import os
import time
import datetime

from pygit2 import clone_repository
from pygit2 import Repository
from pygit2 import GIT_SORT_TOPOLOGICAL, GIT_SORT_REVERSE, GIT_CHECKOUT_SAFE_CREATE

def collectRepo(repo):
	repo_url = repo
	urlChunks = repo_url.split('/')
	repo_path = 'repos/' + urlChunks[len(urlChunks)-1].replace('.git', '').lower()

	if not os.path.exists(repo_path):
		print 'Checking out ' + repo_path
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

def getHist(repo):
	base = Repository(repo)
	base.checkout('HEAD')
	history = []
	for commit in base.walk(base.head.target, GIT_SORT_TOPOLOGICAL | GIT_SORT_REVERSE):
		history.append(commit)
	
	return history

def process(repo, history):
	# GET A REPO ON DISK
	base = Repository(repo)
	base.checkout('HEAD')

	file_xsmall = 0
	file_small = 0
	file_medium = 0
	file_large = 0
	file_xlarge = 0
		
	hunk_xsmall = 0
	hunk_small = 0
	hunk_medium = 0
	hunk_large = 0
	hunk_xlarge = 0

	line_xsmall = 0
	line_small = 0
	line_medium = 0
	line_large = 0
	line_xlarge = 0 
	
	i = 0
	while i < len(history) - 1:
		print '\rDiff#: ' + str(i + 1) + ' of ' + str(len(history)-1),

		t0 = base.revparse_single(history[i].hex)
		t1 = base.revparse_single(history[i+1].hex)
		
		try:
			diff = base.diff(t0,t1)
		except ValueError:
			i += 1
			continue
		
		files = [p for p in diff]
		
		if len(files) == 1:
			file_xsmall += 1
		if len(files) >= 2 and len(files) <= 4:
			file_small += 1
		if len(files) >= 5 and len(files) <= 7:
			file_medium += 1
		if len(files) >= 8 and len(files) <= 10:
			file_large += 1
		if len(files) >= 11:
			file_xlarge += 1
		
		hunksInCommit = 0
		linesInCommit = 0

		for modfile in files:
			hunksInCommit += len(modfile.hunks)
			for hunk in modfile.hunks:
				for line in hunk.lines:
					if line[0] == '-' or line[0] == '+':
						linesInCommit += 1


		if hunksInCommit <= 1:
			hunk_xsmall += 1
		if hunksInCommit >= 2 and hunksInCommit <= 8:
			hunk_small += 1
		if hunksInCommit >= 9 and hunksInCommit <= 17:
			hunk_medium += 1
		if hunksInCommit >= 18 and hunksInCommit <= 26:
			hunk_large += 1
		if hunksInCommit >= 27:
			hunk_xlarge += 1

		if linesInCommit <= 5:
			line_xsmall += 1
		if linesInCommit >= 6 and linesInCommit <= 46:
			line_small += 1
		if linesInCommit >= 47 and linesInCommit <= 106:
			line_medium += 1
		if linesInCommit >= 107 and linesInCommit <= 166:
			line_large += 1
		if linesInCommit >= 167:
			line_xlarge += 1

		i += 1
	print ''

	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('-%Y-%m-%d.%H.%M.%S')
	name = repo.replace('/.git', '') + st + '.txt'
	output = open(name,'w')

	output.write('--------- ' + repo + ' ----------' + '\n')
	output.write('Number of Lines Modified:' + '\n')
	output.write('x-small: ' + str( + line_xsmall) + '\n')
	output.write('small: ' + str(line_small) + '\n')
	output.write('medium: ' + str(line_medium) + '\n')
	output.write('large: ' + str(line_large) + '\n')
	output.write('x-large: ' + str(line_xlarge) + '\n')

	output.write('Number of Files Modified:' + '\n')
	output.write('x-small: ' + str(file_xsmall) + '\n')
	output.write('small: ' + str(file_small) + '\n')
	output.write('medium: ' + str(file_medium) + '\n')
	output.write('large: ' + str(file_large) + '\n')
	output.write('x-large: ' + str(file_xlarge) + '\n')

	output.write('Number of Hunks Per Commit' + '\n')
	output.write('x-small: ' + str(hunk_xsmall) + '\n')
	output.write('small: ' + str(hunk_small) + '\n')
	output.write('medium: ' + str(hunk_medium) + '\n')
	output.write('large: ' + str(hunk_large) + '\n')
	output.write('x-large: ' + str(hunk_xlarge) + '\n')

	output.close()

def commitInfo(repo, history):
	# GET A REPO ON DISK
	base = Repository(repo)
	base.checkout('HEAD')

	# MOVE THROUGH THE SYSTEM HISTORY FROM NEWEST TO OLDEST COMMIT
	for commit in history:
		print 'Date/Time: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(commit.commit_time))
		print 'Comment Hex: ' + commit.hex
		print 'Message: ' + commit.message.rstrip('\n')
		print ''
