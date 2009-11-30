#!/usr/bin/python
#
# This program uses GeoIP to find websites that match `dst_keyword`, which
# are located in `dst_country` country, and even more specifically, which
# are located in `dst_states` state in this country.
#

import GeoIP
from urlparse import urlparse
from xgoogle.search import GoogleSearch, SearchError

class Geo(object):
  GEO_PATH = "/usr/local/geo_ip/GeoLiteCity.dat"

  def __init__(self):
    self.geo = GeoIP.open(Geo.GEO_PATH, GeoIP.GEOIP_STANDARD)

  def detect_by_host(self, host):
    try:
      gir = self.geo.record_by_name(host)
      return {'country': gir['country_code'].lower(),
              'region': gir['region'].lower()}
    except Exception, e:
      return {'country': 'none', 'region': 'none'}

dst_country = 'us'
dst_states = ['ca', 'ny']
dst_keyword = "wicked code"
num_results = 10
final_results = []
geo = Geo()

gs = GoogleSearch(dst_keyword)
gs.results_per_page = 100

seen_websites = []
while len(final_results) < num_results:
  results = gs.get_results()
  domains = [urlparse(r.url).netloc for r in results]
  for d in domains:
    geo_loc = geo.detect_by_host(d)
    if (geo_loc['country'] == dst_country and
                 geo_loc['region'] in dst_states and
                 d not in seen_websites):
      final_results.append((d, geo_loc['region']))
      seen_websites.append(d)
      if len(final_results) == num_results:
        break

print "Found %d websites:" % len(final_results)
for w in final_results:
    print "%s (state: %s)" % w

