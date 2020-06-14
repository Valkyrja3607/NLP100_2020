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
lb=np.array(l["base"])
lp=np.array(l["pos"])
verb_base=lb[lp=="動詞"]

#print(verb_base[:10])

