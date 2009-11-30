#!/usr/bin/python
#
# This program finds how the target_domain ranks for target_keyword keyword.
#
#

import re
from urlparse import urlparse
from xgoogle.search import GoogleSearch, SearchError

target_domain = "catonmat.net"
target_keyword = "python videos"

def mk_nice_domain(domain):
    """
    convert domain into a nicer one (eg. www3.google.com into google.com)
    """
    domain = re.sub("^www(\d+)?\.", "", domain)
    # add more here
    return domain

gs = GoogleSearch(target_keyword)
gs.results_per_page = 100
results = gs.get_results()
for idx, res in enumerate(results):
  parsed = urlparse(res.url)
  domain = mk_nice_domain(parsed.netloc)
  if domain == target_domain:
    print "Ranking position %d for keyword %s on domain %s" % (idx+1, target_keyword, target_domain) 

