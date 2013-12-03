# A prototype for collecting size metrics from various github repositories, including:
#	- LOC per commit
#	- SLOC per commit (LOC ignoring whitespaces and comments)
#	- LOC per hunk
#	- SLOC per hunk
#	- Hunk per commit
#	- Number of files changed per commit
#	- Number of commits per push

from pygit2 import clone_repository
from pygit2 import Repository
from pygit2 import GIT_SORT_TOPOLOGICAL, GIT_SORT_REVERSE, GIT_CHECKOUT_SAFE_CREATE
import os # Used for git commands, changing directory, and removing cloned repositories
import re # Used to match the name of a repository given its github URL
import pprint # Used for pretty printing repo stats
import subprocess # Used for Drew's weird thing

class prototype:
    repo = ""  # Path to a given repository
    name = ""  # Name of a repository
    base = ""  # Repository as defined in pygit2

    # Initialization. Clones the given repository, placing it in the current directory,
    # and changes to the repository directory.
    def init(self, repository):
        self.repo = repository

        # Use regular expressions to match the last instance of a forward slash
        # followed by the name of the repository, which we wish to extract, followed
        # by ".git". 
        m = re.search('/([^/]+).git$', repository)
        if m:
            self.name = m.group(1)
        os.system('git clone ' + self.repo) # Get the repository from GitHub
        self.base = Repository(self.name)
        self.base.checkout('HEAD')

    # Destruction. Remove the given repository from memory.
    def destroy(self):
        os.system('cd ' + self.name)
        os.system('rm -rf ' + self.name)

    # Get total LOC by given repository. 
    def totalRepoLOC(self):
        loc = countDirLOC(self.name)
        return loc

    # Get total commits by a given repository
    def totalRepoCommits(self):
        commits = 0
        for commit in self.base.walk(self.base.head.target, GIT_SORT_TOPOLOGICAL):
            commits = commits + 1
        return commits

    # Get a list of LOC changed per commit
    def locPerCommit(self):
        loc = []
        oldPath = os.popen('pwd')
        os.chdir(self.name)
        sha1 = 0
        sha2 = 0

        # For each commit within the repository
        for commit in self.base.walk(self.base.head.target, GIT_SORT_TOPOLOGICAL):

            # Based on the SHA, use git to show the patch for that commit
            sha1 = sha2
            sha2 = commit.hex
            if sha1 != 0:
                p = os.popen('git diff --shortstat ' + sha1 + ' ' + sha2)
                line = p.readline()

                # line contains "# file changed, # insertions(+), # deletions(-)
                # Use regular expressions to find the number of additions and deletions.
                # Additions are found after ", " and before " insertion". Deletions are
                # found after "(+), " and before " deletion".
                m = re.search(', (.*) insertion', line)
                additions = 0
                deletions = 0
                if m:
                    additions = m.group(1)
                m = re.search('\(\+\), (.*) deletion', line)
                if m:
                    deletions = m.group(1)

                # Get the total and append to array
                modifications = int(additions) + int(deletions)
                loc.append(modifications)

        os.chdir('..')
        return loc


    # Get a list containing the total number of line additions and deletions (including
    # whitespace and comments) contained within each hunk that was changed over t
    def locPerHunk(self):
        loc = []
        history = []

        # Get the hex number for each commit within the repository
        for commit in self.base.walk(self.base.head.target, GIT_SORT_TOPOLOGICAL):
            sha = commit.hex
            history.append(sha)

        # Compare each revision in the history of the repository with the previous rev.
        i = 0
        while i < len(history) - 1:
            t0 = self.base.revparse_single(history[i])
            t1 = self.base.revparse_single(history[i+1])
            diff = self.base.diff(t0,t1)
            patches = [p for p in diff]
            for patch in patches:
                for hunk in patch.hunks:
                   
                    # Check the first character in each hunk line. Only those that have
                    # been modified will contain a '+' (insertion) or '-' (deletion)
                    totalModifications = 0
                    for line in hunk.lines:
                        if line[0] == '-' or line[0] == '+':
                            totalModifications +=1
                    loc.append(totalModifications)
            i += 1
        return loc

    # Get the total number of lines contained within a hunk, including additions, deletions,
    # and surrounding non-changed lines
    def locInHunk(self):
        loc = []
        history = []

        # Get the hex number for each commit within the repository
        for commit in self.base.walk(self.base.head.target, GIT_SORT_TOPOLOGICAL):
            sha = commit.hex
            history.append(sha)

        # Compare each revision in the history of the repository with the previous rev.
        i = 0
        while i < len(history) - 1:
            t0 = self.base.revparse_single(history[i])
            t1 = self.base.revparse_single(history[i+1])
            diff = self.base.diff(t0,t1)
            patches = [p for p in diff]
            for patch in patches:
                for hunk in patch.hunks:
                    totalLines = 0
                    for line in hunk.lines:
                       totalLines += 1
                    loc.append(totalLines)
            i += 1
        return loc

    # Perform a diff between all commits starting from oldest to newest
    #  and compile temp files comprised of only modified lines.
    #  Run cloc on temp files to get sloc for each diff set.
    def slocPerDiff(self):
        # Storage for commit history hashes
        history = []
        
        # Store all slocs
        slocPerDiffs = []

        # Move through the system history from newest to oldest commit
        for commit in self.base.walk(self.base.head.target, GIT_SORT_TOPOLOGICAL | GIT_SORT_REVERSE):
            history.append(commit)

        i = 0
        while i < len(history) - 2:
            sloc = 0
            t0 = self.base.revparse_single(history[i].hex)
            t1 = self.base.revparse_single(history[i+1].hex)
            diff = self.base.diff(t0,t1)
            patches = [p for p in diff]
            for patch in patches:
                hunkfile = open(patch.new_file_path, 'w')
                for hunk in patch.hunks:
                    totesLines = 0
                    totesMods = 0
                    for line in hunk.lines:
                        totesLines += 1
                        if line[0] == '-' or line[0] == '+':
                            totesMods += 1
                            hunkfile.write(line[1])
                hunkfile.close()
            
                output = subprocess.Popen('cloc ' + patch.new_file_path + ' --by-file --csv', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                start = False
                for line in output.stdout.readlines():
                    if line[0] == 'l':
                        start = True
                        continue
                    if start:
                        temp = line.split(',')
                        sloc += int(temp[4].replace('\n', ''))
                        retval = output.wait()
                        os.remove(patch.new_file_path)
            i += 1
            slocPerDiffs.append(str(sloc))
        
        return slocPerDiffs

    # Get a list containing the number of hunks changed per commit
    def hunksPerCommit(self):
        hunks = []
        history = []

        # Get the hex number for each commit within the repository
        for commit in self.base.walk(self.base.head.target, GIT_SORT_TOPOLOGICAL):
            sha = commit.hex
            history.append(sha)

        # Compare each revision in the history of the repository with the previous rev.
        i = 0
        while i < len(history) - 1:
            t0 = self.base.revparse_single(history[i])
            t1 = self.base.revparse_single(history[i+1])
            diff = self.base.diff(t0,t1)
            patches = [p for p in diff]
            for patch in patches:
                hunks.append(len(patch.hunks))
            i += 1

        return hunks


    # Get a list of the number of files changed per commit
    def filesPerCommit(self):
        files = []
        oldPath = os.popen('pwd')
        os.chdir(self.name)
        sha1 = 0
        sha2 = 0

        # For each commit within the repository
        for commit in self.base.walk(self.base.head.target, GIT_SORT_TOPOLOGICAL):

            # Based on the SHA, use git to show the patch for that commit
            sha1 = sha2
            sha2 = commit.hex
            if sha1 != 0:
                p = os.popen('git diff --shortstat ' + sha1 + ' ' + sha2)
                line = p.readline()

                # line contains "# file changed, # insertions(+), # deletions(-)
                # Use regular expressions to find the number of files modified, which
                # are contained first on the line followed by " file"
                m = re.search(' (.*) file', line)
                if m:
                    numFilesChanged = int(m.group(1))
                    files.append(numFilesChanged)

        os.chdir('..')
        return files

    # Print out all stats for the repository
    def printStats(self):
        
        print "-----------" + self.name + "-----------"

        # Stats on entire repository
        repoLOC = self.totalRepoLOC()
        repoCommits = self.totalRepoCommits()

        # Lists by commit
        locPerCommit   = self.locPerCommit()
        slocPerDiff    = self.slocPerDiff()
        hunksPerCommit = self.hunksPerCommit()
        filesPerCommit = self.filesPerCommit()
        
        # Stats for LOC
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

        # Stats for SLOC
        xsmall = 0
        small  = 0
        medium = 0
        large  = 0
        xlarge = 0
        for item in slocPerDiff:
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

        print "Number of Modified SLOC:"
        print "x-small: " + str(xsmall)
        print "small:   " + str(small)
        print "medium:  " + str(medium)
        print "large:   " + str(large)
        print "x-large: " + str(xlarge)

        # Print stats for modified files
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

        # Prints stats for hunks
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

            

# -----------------------------------------------------------------------------------
# Private implementation used within the class:

# Read in a file and count each LOC (including whitespace and commments). Close the
# file and return the count.
def countFileLOC(file):
    counter = 0
    file = open(file, "r")
    for line in file.read().split('\n'):
        counter = counter + 1
    file.close()
    return counter

# Read each file within a directory, including subdirectories via recursion, and 
# count each LOC (including whitespace and comments). Close the files and return 
# the count
def countDirLOC(dir):
    counter = 0
    for file in os.listdir(dir):
        path = os.path.join(dir, file)
        if os.path.isdir(path):
            dcount = countDirLOC(path)
            counter = counter + dcount
        else:
            fcount = countFileLOC(path)
            counter = counter + fcount
    return counter


