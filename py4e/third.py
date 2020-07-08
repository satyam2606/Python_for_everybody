import re
fname=input("Enter the file name")
fhandle=open(fname)
addition=0
numlist=list()
for line in fhandle:
    line=line.rstrip()
    y=re.findall('[0-9]+',line)
    if len(y)<1:continue
    for i in range(len(y)):
        num=int(y[i])
        numlist.append(num)
        addition=addition+num
print("There are",len(numlist),"values with a sum=",addition)
