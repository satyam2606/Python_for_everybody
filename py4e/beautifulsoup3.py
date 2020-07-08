import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl                                               #for errors
ctx=ssl.create_default_context()                          #for errors
ctx.check_hostname=False                                    #for errors
ctx.verify_mode=ssl.CERT_NONE                               #for errors
url=input("enter . . .")
count = int(input("Enter count"))
position=int(input("Enter position"))
#print(url.contents[0])
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')
tags=soup('a')
for i in range(count):
    print(tags.get('href',None))
    link=tags[position].get('href',None)
    print(tags[position].contents[0])
    html=urllib.request.urlopen(link).read()
    soup=BeautifulSoup(html,'html.parser')
    tags=soup('a')


#for i in range(count):
#    html=urllib.request.urlopen(url).read()
#    soup=BeautifulSoup(html,"html.parser")
#    tags=soup("a")
#    link=tags[position].get("href",None)
#    url=link
#    name=tags[position].contents[0]
#    print(name)
