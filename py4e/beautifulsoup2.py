import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,"html.parser")
tag = soup("span")
counts=0
sum=0
for i in tag:
    x=int(i.contents[0])     #we can also use (i.text)
    #print("ATTRS:",i.attrs)
    #print("TAGS:",i)
    counts=counts+1
    sum=sum+x
print(counts)
print(sum)
