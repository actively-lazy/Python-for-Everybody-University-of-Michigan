import urllib
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
print("Retrieving: " + url)
js = json.loads(urllib.request.urlopen(url, context=ctx).read())
print("Retrieved: ", json.dumps(js, indent=2))

sum = 0
for comment in js['comments']:
    sum += int(comment['count'])

print(sum)
