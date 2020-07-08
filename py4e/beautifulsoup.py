import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl                                               #for errors
ctx=ssl.create_default_context()                          #for errors
ctx.check_hostname=False                                    #for errors
ctx.verify_mode=ssl.CERT_NONE                               #for errors
url=input("enter . . .")
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')
tags=soup('a')
for tag in tags:
    print(tag.get('href',None))
