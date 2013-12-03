#!/usr/bin/env python2

# Used to test the functionality of "prototype.py", which contains various size metrics
# computed on a given github repository.

from prototype import prototype

repos = [
    "https://github.com/octocat/Spoon-Knife.git",
#    "https://github.com/django/django.git",
    "https://github.com/joyent/node.git",
    "https://github.com/mono/mono.git",
    "https://github.com/ruby/ruby.git",
    "https://github.com/python-git/python.git",
    "https://github.com/mirrors/gcc.git",
    "https://github.com/pld-linux/koffice.git",
    "https://github.com/GNOME/gimp.git",
    "https://github.com/chromium/chromium.git",
    "https://github.com/linuxmint/Cinnamon.git",
    "https://github.com/torvalds/linux.git",
    "https://github.com/apache/hadoop-common.git",
    "https://github.com/visionmedia/express.git",
    "https://github.com/freebsd/freebsd.git",
]

for repo in repos:
    monoRepo = prototype()
    monoRepo.init(repo)
    monoRepo.printStats()
