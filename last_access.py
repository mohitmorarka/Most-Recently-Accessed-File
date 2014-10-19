#!/usr/bin/env python

import sys, os.path, time

"""
Comments-
1)	Script takes a list of filenames as arguments.
2)	An error message is printed if the path to the file is not found.
3)	An error message is printed to handle anything that is not a file.
4)	It also assumes that spaces for the files have been escaped.

"""

class LastAccess:

  def __init__(self, paths):
    self.fileVars = []
    self.recentvars = []
    self.loadfileVars(paths)

  def loadfileVars(self, paths):
    for path in paths:
      if os.path.isfile(path):
        self.fileVars.append({ 'name': path,  'last_accessed': os.path.getatime( path ) })
      else:
        print "not a file." % path

  def recentVars(self):
    if len(self.fileVars) > 0:
      self.recentvars = sorted(self.fileVars, key=itemgetter('last_accessed'), reverse = True)

  def printLastAccess(self):
    self.recentVars()
    if len(self.recentvars) > 0:
      print "%s" % self.recentvars[0]['name']
    else:
      print "-> no file available."

# Test class if running directly.
if __name__ == '__main__':
  Access = LastAccess(sys.argv[1:])
  Access.printLastAccess()
