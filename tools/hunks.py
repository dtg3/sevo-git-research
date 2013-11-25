from pygit2 import clone_repository
from pygit2 import Repository
from pygit2 import GIT_SORT_TOPOLOGICAL, GIT_SORT_REVERSE, GIT_CHECKOUT_SAFE_CREATE
import os
import sh
import subprocess
import time

repo_url = 'https://github.com/octocat/Spoon-Knife.git'
repo_path = 'spoon-knife'

if not os.path.exists(repo_path):
    repo = clone_repository(repo_url, repo_path)

base = Repository(repo_path + '/.git')
base.checkout('HEAD')

history = []
# Display Commits Newest to Oldest
for commit in base.walk(base.head.target, GIT_SORT_TOPOLOGICAL):
    #print commit.hex
    #print commit.message
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(commit.commit_time))
    history.append(commit.hex)

#print '-----------------------------------------------------------'

# Display Commits Oldest to Newest
for commit in base.walk(base.head.target, GIT_SORT_TOPOLOGICAL | GIT_SORT_REVERSE):
    pass
#    print commit.hex
#    print base.revparse_single(commit.hex).message
#    print commit.commit_time
#    print commit.commit_time_offset

git = sh.git.bake(_cwd='/home/heather/research/spoon-knife')

for point in history:
    git.checkout(point)
#    print subprocess.check_output(['ohcount', 'spoon-knife'])

git.checkout(history[0])

i = 0
while i < len(history) - 2:
    t0 = base.revparse_single(history[i])
    t1 = base.revparse_single(history[i+1])
    diff = base.diff(t0,t1)
    patches = [p for p in diff]
    for patch in patches:
        print 'NUM HUNKS: ' + str(len(patch.hunks))
        for hunk in patch.hunks:
#            print hunk.lines
            totesLines = 0
            totesMods = 0
            for line in hunk.lines:
                totesLines += 1
                if line[0] == '-' or line[0] == '+':
                    totesMods += 1
                    print line
            print 'TOTAL LINES: ' + str(totesLines)
            print 'TOTAL MODS: ' + str(totesMods)
#            print 'OLD: ' + str(hunk.old_lines)
#            print '=---------------='
#            print 'NEW: ' + str(hunk.new_lines)
    i += 1
