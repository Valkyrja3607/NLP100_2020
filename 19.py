path=__file__
f=open(path+"/../"+"popular-names.txt")
l=[]
import numpy as np
col1=np.array([i.split("\t") for i in f.readlines()])[:,0]
import collections
cnt=collections.Counter(col1)
f=open(path+"/../"+"popular-names.txt")
for i in f.readlines():
    a,b,c,d=i.split("\t")
    l.append([cnt[a],a,b,int(c),d.replace("\n","")])
l.sort(reverse=True)
l=np.array(l)[:,1:]

