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
from operator import itemgetter
from xgoogle.search import GoogleSearch, SearchError

args = sys.argv[1:]
if not args:
  print "Usage: google_fight.py keyword one, keyword two, ..."
  sys.exit(1)

keywords = [k.strip() for k in ' '.join(args).split(',')]
try:
  results = [(k, GoogleSearch('"%s"' % k).num_results) for k in keywords]
except SearchError, e:
  print "Google search failed: %s" % e
  sys.exit(1)

results.sort(key=itemgetter(1), reverse=True)
for res in results:
    print "%s: %d" % res

