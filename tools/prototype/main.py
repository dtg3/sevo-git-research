#!/usr/bin/env python2

# Used to test the functionality of "prototype.py", which contains various size metrics
# computed on a given github repository.

from prototype import prototype

monoRepo = prototype()
monoRepo.init("https://github.com/mono/mono.git")
monoRepo.printStats()
monoRepo.destroy()

nodeRepo = prototype()
nodeRepo.init("https://github.com/joyent/node.git")
nodeRepo.printStats()
nodeRepo.destroy()

rubyRepo = prototype()
rubyRepo.init("https://github.com/ruby/ruby.git")
rubyRepo.printStats()
rubyRepo.destroy()

pythonRepo = prototype()
pythonRepo.init("https://github.com/python-git/python.git")
pythonRepo.printStats()
pythonRepo.destroy()

gccRepo = prototype()
gccRepo.init("https://github.com/mirrors/gcc.git")
gccRepo.printStats()
gccRepo.destroy()

officeRepo = prototype()
officeRepo.init(" https://github.com/pld-linux/koffice.git")
officeRepo.printStats()
officeRepo.destroy()

gimpRepo = prototype()
gimpRepo.init("https://github.com/GNOME/gimp.git")
gimpRepo.printStats()
gimpRepo.destroy()

chromiumRepo = prototype()
chromiumRepo.init("https://github.com/chromium/chromium.git")
chromiumRepo.printStats()
chromiumRepo.destroy()

cinnamonRepo = prototype()
cinnamonRepo.init("https://github.com/linuxmint/Cinnamon.git")
cinnamonRepo.printStats()
cinnamonRepo.destroy()

linuxRepo = prototype()
linuxRepo.init("https://github.com/torvalds/linux.git")
linuxRepo.printStats()
linuxRepo.destroy()

hadoopRepo = prototype()
hadoopRepo.init("https://github.com/apache/hadoop-common.git")
hadoopRepo.printStats()
hadoopRepo.destroy()

djangoRepo = prototype()
djangoRepo.init("https://github.com/django/django.git")
djangoRepo.printStats()
djangoRepo.destroy()

expressRepo = prototype()
expressRepo.init("https://github.com/visionmedia/express.git")
expressRepo.printStats()
expressRepo.destroy()

freebsdRepo = prototype()
freebsdRepo.init("https://github.com/freebsd/freebsd.git")
freebsdRepo.printStats()
freebsdRepo.destroy()


'''
# Get total LOC within the repo
loc = repo.totalRepoLOC()
print "Total number of LOC in this repository: " + str(loc)

# Get total number of commits for the repo
commits = repo.totalRepoCommits()
print "Total number of commits in this repository: " + str(commits)

# Get a list containing the number of LOC changed for each commit
locPerCommit = repo.locPerCommit()

xsmall = 0
small  = 0
medium = 0
large  = 0
xlarge = 0
for item in locPerCommit:
    if (item >= 0 and item <= 5):
        xsmall += 1
    if (item >= 6 and item <= 46):
        small += 1
    if (item >= 47 and item <= 106):
        medium += 1
    if (item >= 107 and item <= 166):
        large += 1
    if (item >= 167):
        xlarge += 1
    
print "Number of Modified Lines:"
print "x-small: " + str(xsmall)
print "small:   " + str(small)
print "medium:  " + str(medium)
print "large:   " + str(large)
print "x-large: " + str(xlarge)

# Get a list containing the number of files changed for each commit
filesPerCommit = repo.filesPerCommit()

xsmall = 0
small  = 0
medium = 0
large  = 0
xlarge = 0
for item in filesPerCommit:
    if (item == 1):
        xsmall += 1
    if (item >= 2 and item <= 4):
        small += 1
    if (item >= 5 and item <= 7):
        medium += 1
    if (item >= 8 and item <= 10):
        large += 1
    if (item >= 11):
        xlarge += 1

print "Number of modified files:"
print "x-small: " + str(xsmall)
print "small:   " + str(small)
print "medium:  " + str(medium)
print "large:   " + str(large) 
print "x-large: " + str(xlarge)

# Get a list containing the number of SLOC changed for each commit
# slocPerCommit = Repository.slocPerCommit()

# Get a list containing the number of hunks changed for each commit
hunksPerCommit = repo.hunksPerCommit()

xsmall = 0
small  = 0
medium = 0
large  = 0
xlarge = 0
for item in hunksPerCommit:
    if (item >= 0 and item <= 1):
        xsmall += 1
    if (item >= 2 and item <= 8):
        small += 1
    if (item >= 9 and item <= 17):
        medium += 1
    if (item >= 18 and item <= 26):
        large += 1
    if (item >= 27):
        xlarge += 1

print "Number of hunks per commit:"
print "x-small: " + str(xsmall)
print "small:   " + str(small)
print "medium:  " + str(medium)
print "large:   " + str(large) 
print "x-large: " + str(xlarge)

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
''' 
