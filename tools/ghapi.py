import urllib2
import json
import collections

url = 'https://api.github.com/repos/octocat/Spoon-Knife/pulls'

response = urllib2.urlopen(url)
jsponse = json.loads(response.read(), object_pairs_hook=collections.OrderedDict)

print json.dumps(jsponse, indent=2)

response.close()
