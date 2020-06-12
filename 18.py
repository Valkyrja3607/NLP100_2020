path=__file__
f=open(path+"/../"+"popular-names.txt")
l=[]
for i in f.readlines():
    a,b,c,d=i.split("\t")
    l.append([a,b,int(c),d.replace("\n","")])
from operator import itemgetter
l.sort(key=itemgetter(2))
print(l)
