import argparse
import sys
import os
import sqlite3
import imp
from gitreap import *

def main(argv):
  # CLI MAGIC
  parser = argparse.ArgumentParser(description='Aquire a GitHub Repository and Analyze its comment history')

  # ADD ARGS HERE
  parser.add_argument('-r','--repo', help='Process individual repo')
  parser.add_argument('-l','--repoList', help='Process repo text file link')

  # TAKE CLI ARGS AND PARSE ALL THE THINGS
  cliOpt = parser.parse_args(argv[1:])

  if cliOpt.repo:
    print collectRepo(cliOpt.repo)

  if cliOpt.repoList:
    collectAllRepos(cliOpt.repoList)

  # RUN MAIN - MAKES IT FEEL MORE LIKE A REGUALR C++ APP
if __name__ == '__main__':
  main(sys.argv)
