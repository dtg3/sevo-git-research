#!/usr/bin/env python2

# Used to test the functionality of "prototype.py", which contains various size metrics
# computed on a given github repository.

from prototype import prototype

monoRepo = prototype()
monoRepo.init("https://github.com/mono/mono.git")
monoRepo.printStats()

nodeRepo = prototype()
nodeRepo.init("https://github.com/joyent/node.git")
nodeRepo.printStats()

rubyRepo = prototype()
rubyRepo.init("https://github.com/ruby/ruby.git")
rubyRepo.printStats()

pythonRepo = prototype()
pythonRepo.init("https://github.com/python-git/python.git")
pythonRepo.printStats()

gccRepo = prototype()
gccRepo.init("https://github.com/mirrors/gcc.git")
gccRepo.printStats()

officeRepo = prototype()
officeRepo.init(" https://github.com/pld-linux/koffice.git")
officeRepo.printStats()

gimpRepo = prototype()
gimpRepo.init("https://github.com/GNOME/gimp.git")
gimpRepo.printStats()

chromiumRepo = prototype()
chromiumRepo.init("https://github.com/chromium/chromium.git")
chromiumRepo.printStats()

cinnamonRepo = prototype()
cinnamonRepo.init("https://github.com/linuxmint/Cinnamon.git")
cinnamonRepo.printStats()

linuxRepo = prototype()
linuxRepo.init("https://github.com/torvalds/linux.git")
linuxRepo.printStats()

hadoopRepo = prototype()
hadoopRepo.init("https://github.com/apache/hadoop-common.git")
hadoopRepo.printStats()

djangoRepo = prototype()
djangoRepo.init("https://github.com/django/django.git")
djangoRepo.printStats()

expressRepo = prototype()
expressRepo.init("https://github.com/visionmedia/express.git")
expressRepo.printStats()

freebsdRepo = prototype()
freebsdRepo.init("https://github.com/freebsd/freebsd.git")
freebsdRepo.printStats()
