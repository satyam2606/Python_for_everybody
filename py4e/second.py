#name = input("Enter file:")
name = "mbox-short.txt"
handle = open(name)
counts=dict()
lst=list()
for line in handle:
    line=line.rstrip()
    words=line.split()
    if len(words)<1 or words[0]!="From":continue
    else:
        word=words[5].split(':')
        #print(word)
        counts[word[0]]=counts.get(word[0],0)+1
#print(word,counts)
#print(sorted(counts.items()))
for k,v in sorted(counts.items()):
    print(k,v)
#for k,v in counts.items():
#    lst.append((k,v))
#lst.sort()
#for k,v in lst:
    #print(k,v)
