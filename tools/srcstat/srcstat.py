#!/usr/bin/env python2

import argparse
import sys
import os
import imp

from gitreap import *

repos = []
history = []

def main(argv):
  # CLI MAGIC
  parser = argparse.ArgumentParser(description='Aquire a GitHub Repository and Analyze its comment history')

  # ADD ARGS HERE
  parser.add_argument('-r','--repo', help='Process individual repo')
  parser.add_argument('-l','--repoList', help='Process repo text file list')

  # TAKE CLI ARGS AND PARSE ALL THE THINGS
  cliOpt = parser.parse_args(argv[1:])

  if cliOpt.repo:
    repos.append(collectRepo(cliOpt.repo))

  if cliOpt.repoList:
    repos.extend(collectAllRepos(cliOpt.repoList))

  for repo in repos:
    print repo
    hist = getHist(repo)
    process(repo, hist)
    #commitInfo(repo)

  # RUN MAIN - MAKES IT FEEL MORE LIKE A REGUALR C++ APP
if __name__ == '__main__':
  main(sys.argv)
