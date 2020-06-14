import MeCab
path=__file__
neko=path+"/../"+"neko.txt"
neko_mecab=path+"/../"+"neko.txt.mecab"

#形態素解析
m=MeCab.Tagger("-MeCab")
with open(neko,encoding='utf-8') as f:
    for sentence in f:
        mecabed_sentence=m.parse(sentence)
        with open(neko_mecab,mode='a',encoding='utf-8') as new_file:
            new_file.write(mecabed_sentence)

