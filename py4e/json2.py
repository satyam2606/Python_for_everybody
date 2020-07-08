import urllib.request, urllib.parse, urllib.error
import json
y=[]
url=input("Enter the url...")
html=urllib.request.urlopen(url).read()
info=json.loads(html)
#print(len(info))
#print(info)
comment=info["comments"]
for i in comment:
    y.append(i["count"])
print(sum(y))
