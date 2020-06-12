import json

path=__file__
f=open(path+"/../"+"jawiki-country.json","r",encoding="utf-8_sig")
for i in f:
    data=json.loads(i)
    if data["title"]=="イギリス":
        print(data["text"])