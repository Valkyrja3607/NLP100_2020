import json
import re
path=__file__
f=open(path+"/../"+"jawiki-country.json","r",encoding="utf-8_sig")
text=""
for i in f:
    data=json.loads(i)
    if data["title"]=="イギリス":
        text=data["text"]
for i in text.split("\n"):
    if re.match(r'^\[\[Category:.+\]\]$',i):
        print(re.match(r'^\[\[Category:(.*)\]\]$',i).group(1).split("|")[0])