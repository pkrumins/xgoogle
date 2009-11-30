#!/usr/bin/python
#
# Peteris Krumins (peter@catonmat.net)
# http://www.catonmat.net  --  good coders code, great reuse
# 
# A Google Fight program. v1.0
#
# Released under GNU GPL
#
# http://www.catonmat.net/blog/python-library-for-google-search
#

import sys
from xgoogle.search import GoogleSearch, SearchError

args = sys.argv[1:]
if len(args) < 2:
 print 'Usage: google_fight.py "keyword 1" "keyword 2"'
 sys.exit(1)

try:
  n0 = GoogleSearch('"%s"' % args[0]).num_results
  n1 = GoogleSearch('"%s"' % args[1]).num_results
except SearchError, e:
  print "Google search failed: %s" % e
  sys.exit(1)

if n0 > n1:
  print "%s wins with %d results! (%s had %d)" % (args[0], n0, args[1], n1)
elif n1 > n0:
  print "%s wins with %d results! (%s had %d)" % (args[1], n1, args[0], n0)
else:
  print "It's a tie! Both keywords have %d results!" % n1

