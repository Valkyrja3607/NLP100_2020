import json
import re
import urllib.parse, urllib.request
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
    j=re.sub("\[\[ファイル:([^|]+)\|([^|\]]+)\|([^\]]+)\]\]","\g<3>",j)
    j=re.sub("\{\{lang\|[a-z]{2,}\|([^}]+)\}\}","\g<1>",j)
    j=re.sub("\[([^ ]+) ([^\]]+)\]","\g<2>",j)
    j=re.sub("<([a-z]+)( )?/>","",j)
    j=re.sub("<([a-z]+)( [^>]+)?>","",j)
    j=re.sub("</([a-z]+)>","",j)
    ans[i]=j

flag=ans["国旗画像 "]
url = 'https://www.mediawiki.org/w/api.php?'+'action=query'+'&titles=File:'+urllib.parse.quote(flag)+'&format=json'+'&prop=imageinfo'+'&iiprop=url'

#MediaWikiのサービスへリクエスト送信
request=urllib.request.Request(url,headers={'User-Agent':'NLP100_Python(@segavvy)'})
connection=urllib.request.urlopen(request)

#jsonとして受信
data=json.loads(connection.read().decode())

#URL取り出し
url=data['query']['pages'].popitem()[1]['imageinfo'][0]['url']
print(url)