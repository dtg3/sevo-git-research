import os
import time

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

def traverse(repo):
	base = Repository(repo)
	base.checkout('HEAD')

	history = []

	for commit in base.walk(base.head.target, GIT_SORT_TOPOLOGICAL):
		print 'Date/Time: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(commit.commit_time))
		print 'Message: ' + commit.message.rstrip('\n')
		history.append(commit.hex)
		print 'Files Changed:'
		for changedFile in commit.tree:
			print changedFile.name
