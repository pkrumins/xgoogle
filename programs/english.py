#!/usr/bin/python
#
# Peteris Krumins (peter@catonmat.net)
# http://www.catonmat.net  --  good coders code, great reuse
#

# Given a query such as "this is a * night", this program uses xgoogle to
# search for this on google, find 100 results, and sort the results by number
# of appearances.
#
# For example, it may outout:
# 15 "this is a cold night"
# 8 "this is a romantic night"
# 5 "this is a nice night"
# ... etc.
#
# This way you can quickly find adjectives associated with night.
#

import itertools
import operator
import sys
import re
from xgoogle.search import GoogleSearch, SearchError, ParseError

def count_results(results):
    return dict((len(list(group)), item) for item, group in itertools.groupby(sorted(results)))

def print_results(results):
    sr = sorted(results.iteritems(), key=operator.itemgetter(0), reverse=True)
    for r in sr:
        print "%d\t%s" % r

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print 'Error: usage %s "phrase with * in it"' % sys.argv[0]
        sys.exit(1)
    if args > 1:
        args = ' '.join(args)
    query = '"%s"' % args
    gs = GoogleSearch(query)
    gs.results_per_page = 100
    results = gs.get_results()
    args_re = args.replace('*', '.*?')
    filter_re = re.compile(args_re, re.I)
    frf = filter_re.findall
    nomnomnom = []
    for r in results:
        descs = filter_re.findall(r.desc)
        titles = filter_re.findall(r.title)
        nomnomnom += [x.lower().encode('utf-8') for x in descs + titles]
    results = count_results(nomnomnom)
    print_results(results)

