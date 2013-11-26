import argparse
import sys
import os
import sqlite3
import imp
from sets import Set
from gitreap import *

currentRepos = Set()

def main(argv):

    # CLI MAGIC
    parser = argparse.ArgumentParser(description='Aquire a GitHub repository and analyze its comment history')
    # ADD ARGS HERE
    parser.add_argument('-r','--repo', help='Description for foo argument')
    parser.add_argument('-l','--fileList', help='Supply a list of repositories to analyze in txt format')
    
    # TAKE CLI ARGS AND PARSE ALL THE THINGS
    cliOpt = parser.parse_args(argv[1:])

    if cliOpt.repo != '':
        pass

    if cliOpt.fileList != '':
        pass
    
# RUN MAIN - MAKES IT FEEL MORE LIKE A REGUALR C++ APP
if __name__ == '__main__':
  # PRELOAD DATA IF ANY
  if os.path.exists('state/repos'):
    currentRepos = pickle.load('state/repos')

  main(sys.argv)
