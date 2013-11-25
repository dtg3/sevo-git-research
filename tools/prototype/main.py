# Used to test the functionality of "prototype.py", which contains various size metrics
# computed on a given github repository.

from prototype import prototype

# Initialize with a given repository
repo = prototype()
repo.init("git://github.com/libgit2/pygit2.git")

# Get total LOC within the repo
loc = repo.totalRepoLOC()
print "Total number of LOC in this repository: " + str(loc)

# Get total number of commits for the repo
commits = repo.totalRepoCommits()
print "Total number of commits in this repository: " + str(commits)

# Get a list containing the number of LOC changed for each commit
locPerCommit = repo.locPerCommit()
print "List of LOC per commit is:"
print (locPerCommit)

# Get a list containing the number of files changed for each commit
filesPerCommit = repo.filesPerCommit()
print "List of number of files changed per commit:"
print (filesPerCommit)

# Get a list containing the number of SLOC changed for each commit
# slocPerCommit = Repository.slocPerCommit()

# Get a list containing the number of hunks changed for each commit
hunksPerCommit = repo.hunksPerCommit()
print "List of hunks per commit is:"
print (hunksPerCommit)

# Get a list containing the number of LOC changed for each hunk
locPerHunk = repo.locPerHunk()
print "list of LOC per hunk:"
print (locPerHunk)

# Get a list containing the total LOC in each hunk
locInHunk = repo.locInHunk()
print "List of LOC in each hunk."
print (locInHunk)

# Get a list containing the number of SLOC changed for each hunk
# slocPerHunk = repo.slocPerHunk()

# Get a list containing the number of commits per push to the repository
# commitsPerPush = Repository.commitsPerPush()

# Pretty prety all above stats contained:
#Repository: <name>
#URL: <url to repo>
#   ------------------
#KLOC:
#Commits:
#------------------
#Stats by commit
#LOC:
#SLOC:
#Hunk:
#------------------
#Stats by hunk
#LOC:
#SLOC:
#------------------
#Stats by push
#Commits:

# repo.printStats()

repo.destroy()
