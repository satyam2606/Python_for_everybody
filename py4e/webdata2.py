import urllib.request, urllib.parse, urllib.error
fhand=urllib.request.urlopen("http://data.pr4e.org/intro-short.txt")
counts=dict()
list=[]
for lines in fhand:
    lines=lines.decode().rstrip("")
    line=lines.split()
    for word in line:
        counts[word]=counts.get(word,0)+1
#for k in counts:
#    print(k,counts[k])
bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigcount=count
        bigword=word
print(bigword,bigcount)
