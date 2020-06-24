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
lp=l["pos"]

res=[]
for i,j in enumerate(ls):
    if j=="の":
        if lp[i-1]==lp[i+1]=="名詞":
            res.append(ls[i-1]+"の"+ls[i+1])

#print(res[:10])


