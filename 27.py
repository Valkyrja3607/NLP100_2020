import json
import re
path=__file__
f=open(path+"/../"+"jawiki-country.json","r",encoding="utf-8_sig")
text=""
for i in f:
    data=json.loads(i)
    if data["title"]=="イギリス":
        text=data["text"]
res={}
for i in text.split("\n"):
    if re.match(r'\|(.+)=(.*)',i):
        s=re.match(r'\|(.+)=(.*)',i)
        if "style" not in s.group(1) and s.group(1)!="注記 ":
            res[s.group(1)]=s.group(2).strip()

ans={}
for i in res:
    j=res[i]
    j=re.sub("[']{2,4}","",j)
    j=re.sub("\[\[(?:[^:\]]+?\|)?([^:]+?)\]\]","\1",j)
    ans[i]=j

print(json.dumps(ans,indent=4,ensure_ascii=False))