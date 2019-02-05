import urllib
import ssl
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
print("Retrieving: " + url)
xml = urllib.request.urlopen(url, context=ctx).read()
print("Data: \n" + xml.decode())
tree = ET.fromstring(xml)
counts = tree.findall('.//count')

sum = 0
for count in counts:
    sum += int(count.text)

print(sum)
