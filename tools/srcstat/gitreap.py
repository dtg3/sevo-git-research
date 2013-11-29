import os
import time
import subprocess

from pygit2 import clone_repository
from pygit2 import Repository
from pygit2 import GIT_SORT_TOPOLOGICAL, GIT_SORT_REVERSE, GIT_CHECKOUT_SAFE_CREATE

def collectRepo(repo):
	repo_url = repo
	urlChunks = repo_url.split('/')
	repo_path = 'repos/' + urlChunks[len(urlChunks)-1].replace('.git', '').lower()

	if not os.path.exists(repo_path):
		clone_repository(repo_url, repo_path)
	else:
		print 'Repository ' + repo_path + ' already exists!'

	return repo_path + '/.git'

def collectAllRepos(repos):
	repoList = open(repos,'r')
	currentRepos = []

	lines = repoList.readlines()
	for line in lines:
		currentRepos = collectRepo(line.rstrip())
	
	repoList.close()
	return currentRepos

def hunks(repo):
	# GET A REPO ON DISK
	base = Repository(repo)
	base.checkout('HEAD')

	# STORAGE FOR COMMIT HEX VALUES
	history = []

	# MOVE THROUGH THE SYSTEM HISTORY FROM NEWEST TO OLDEST COMMIT
	for commit in base.walk(base.head.target, GIT_SORT_TOPOLOGICAL | GIT_SORT_REVERSE):
		history.append(commit)

	i = 0
	while i < len(history) - 2:
		t0 = base.revparse_single(history[i].hex)
		t1 = base.revparse_single(history[i+1].hex)
		diff = base.diff(t0,t1)
		patches = [p for p in diff]
		for patch in patches:
			print 'OLD FILE NAME: ' + patch.old_file_path
			print 'NEW FILE NAME: ' + patch.new_file_path
			print 'NUM HUNKS: ' + str(len(patch.hunks))
			for hunk in patch.hunks:
				totesLines = 0
				totesMods = 0
				for line in hunk.lines:
					totesLines += 1
					if line[0] == '-' or line[0] == '+':
						totesMods += 1
						print line
				print 'TOTAL LINES: ' + str(totesLines)
				print 'TOTAL MODS: ' + str(totesMods)
		print ''
		i += 1
	print ''

def commitInfo(repo):
	# GET A REPO ON DISK
	base = Repository(repo)
	base.checkout('HEAD')

	# MOVE THROUGH THE SYSTEM HISTORY FROM NEWEST TO OLDEST COMMIT
	for commit in base.walk(base.head.target, GIT_SORT_TOPOLOGICAL | GIT_SORT_REVERSE):
		print 'Date/Time: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(commit.commit_time))
		print 'Comment Hex: ' + commit.hex
		print 'Message: ' + commit.message.rstrip('\n')
		print ''
		
def getLOCS(repo):
	#for repo in repos:
	# call(["ls", "-l"])
	# cloc [directory] --by-file -csv
	output = subprocess.Popen('cloc ' + repo.replace('.git', '') + ' --by-file --csv', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	start = False
	for line in output.stdout.readlines():
		if line[0] == 'l':
			start = True
			
		if start:
			print line,
	retval = output.wait()