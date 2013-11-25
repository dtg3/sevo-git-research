from pygit2 import clone_repository
from pygit2 import Repository
from pygit2 import GIT_SORT_TOPOLOGICAL, GIT_SORT_REVERSE, GIT_CHECKOUT_SAFE_CREATE
import os
import sh
import subprocess
import csv

repo_url = 'https://github.com/octocat/Spoon-Knife.git'
urlChunks = repo_url.split('/')
repo_path = urlChunks[len(urlChunks)-1].replace('.git', '').lower()

#file = open(repo_path + '.csv', 'wb')
#csvWriter = csv.writer(file)

if not os.path.exists(repo_path):
    repo = clone_repository(repo_url, repo_path)

base = Repository(repo_path + '/.git')
base.checkout('HEAD')

history = []
# Display Commits Newest to Oldest
for commit in base.walk(base.head.target, GIT_SORT_TOPOLOGICAL):
    #print commit.hex
    #print commit.message
    #print commit.commit_time
    #print commit.commit_time_offset
    history.append(commit.hex)
'''
print '-----------------------------------------------------------'

# Display Commits Oldest to Newest
for commit in base.walk(base.head.target, GIT_SORT_TOPOLOGICAL | GIT_SORT_REVERSE):
    print commit.hex
    print base.revparse_single(commit.hex).message
    print commit.commit_time
    print commit.commit_time_offset
'''
git = sh.git.bake(_cwd='/home/drew/research/spoon-knife')

for point in history:
    git.checkout(point)
    ohCountResults = subprocess.check_output(['ohcount', 'spoon-knife'])
    ohCountResults = ohCountResults.split('\n')0

    for result in ohCountResults:
        print ' '.join(result.split())
git.checkout(history[0])
