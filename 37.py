import MeCab
import re
path=__file__
neko=path+"/../"+"neko.txt"
neko_mecab=path+"/../"+"neko.txt.mecab"

with open(neko_mecab,encoding='utf-8') as mecabed:
    tmp=[]
    for line in mecabed:
        tmp.append(line)
    text="".join(tmp)

pattern=re.compile(r"(?P<surface>.+?)\t(?P<pos>.+?),(?P<pos1>.+?),.+?,.+?,.+?,.+?,(?P<base>.+?),.+?,.+?\n")
c=re.findall(pattern,text) 

l={}
l["surface"]=[]
l["pos"]=[]
l["pos1"]=[]
l["base"]=[]
for s,p,p1,b in c:
    l["surface"].append(s)
    l["pos"].append(p)
    l["pos1"].append(p1)
    l["base"].append(b)

import numpy as np
ls=l["surface"]
import collections
c=collections.Counter()
tmp=set()
for i in ls:
    if i!="。":
        tmp.add(i)
    else:
        if "猫" in tmp:
            for j in tmp:
                if j!="猫":
                    c[j]+=1
        tmp=set()
res=np.array(c.most_common())
print(res[:10])
import matplotlib.pyplot as plt
x=res[:10][:,0]
y=res[:10][:,1]
plt.bar(x,y,align="center")

plt.show()


