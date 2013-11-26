import argparse
import sys
import os
import sqlite3
import imp
from pygit2 import clone_repository
from pygit2 import Repository
from pygit2 import GIT_SORT_TOPOLOGICAL, GIT_SORT_REVERSE, GIT_CHECKOUT_SAFE_CREATE

def main(argv):

    # CLI MAGIC
    parser = argparse.ArgumentParser(description='Aquire a GitHub Repository and Analyze its comment history')
    # ADD ARGS HERE
    parser.add_argument('-r','--repo', help='Description for foo argument')
    
    # TAKE CLI ARGS AND PARSE ALL THE THINGS
    cliOpt = parser.parse_args(argv[1:])

    '''
    # COLOR FONTING FOR TERMINAL
    try:
        imp.find_module('colorama')
        colorful = True
        from colorama import init, Fore, Back, Style
        init()
        if cliOpt.repo:
            print cliOpt.repo
    except ImportError:
        colorful = False
        print 'Nope'
    '''

    
    
# RUN MAIN - MAKES IT FEEL MORE LIKE A REGUALR C++ APP
if __name__ == '__main__':
  main(sys.argv)
