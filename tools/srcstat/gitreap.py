import os
import time

from pygit2 import clone_repository
from pygit2 import Repository
from pygit2 import GIT_SORT_TOPOLOGICAL, GIT_SORT_REVERSE, GIT_CHECKOUT_SAFE_CREATE
from subprocess import *

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

def traverse(repo):
	# GET A REPO ON DISK
	base = Repository(repo)
	base.checkout('HEAD')

	# STORAGE FOR COMMIT HEX VALUES
	history = []

	# MOVE THROUGH THE SYSTEM HISTORY FROM NEWEST TO OLDEST COMMIT
	previousCommit = None
	for commit in base.walk(base.head.target, GIT_SORT_TOPOLOGICAL):
		history.append(commit.hex)

		if previousCommit:
			# Need two changesets to create a diff
			changeSet1 = base.revparse_single(previousCommit.hex)
			changeSet2 = base.revparse_single(commit.hex)
			diff = base.diff(changeSet1,changeSet2)

			# From the diff, get all the patches
			patches = [p for p in diff]
			
			for patch in patches:
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
		else:
			previousCommit = commit

		print 'Date/Time: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(commit.commit_time))
		print 'Message: ' + commit.message.rstrip('\n')
		print 'Files Changed:'
		for changedFile in commit.tree:
			print changedFile.name

# WALK THROUGH THE REPOS TO GET REPO WIDE LOC STATS
def getLOCS(repos):
	for repo in repos:
		call(["ls", "-l"])
		# cloc [directory] --by-file -csv
		ouput = subprocess.Popen('cloc', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		for line in p.stdout.readlines():
			print line,
		retval = p.wait()

# WALK THROUGH THE REPOS TO GET REPO WIDE LOC STATS
def getLOCS(repos):
	for repo in repos:
		call(["ls", "-l"])
		# cloc [directory] --by-file -csv
		ouput = subprocess.Popen('cloc', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		for line in p.stdout.readlines():
			print line,
		retval = p.wait()