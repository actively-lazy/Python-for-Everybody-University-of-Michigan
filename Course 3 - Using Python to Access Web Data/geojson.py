import urllib
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

address = input('Enter location: ')

# encode the parameters to get url
parms = dict()
parms['address'] = address
parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)

print("Retrieving: " + url)
# js = json.loads(urllib.request.urlopen(url, context=ctx).read().decode())
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

js = json.loads(data)
print("Retrieved: ", json.dumps(js, indent=2))


print(js['results'][0]['place_id'])


