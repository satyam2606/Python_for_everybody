import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
sum=0
url=input("Enter the url to open")
html = urllib.request.urlopen(url).read()
tree=ET.fromstring(html)
y= tree.findall("comments/comment/count")
for num in y:
    sum=sum+int(num.text)
print(sum)
