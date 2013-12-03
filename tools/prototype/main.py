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
