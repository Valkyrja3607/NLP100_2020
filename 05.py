s="I am an NLPer"
def word_n_gram(s,n):
    l=s.split()
    res=[l[i:i+n]for i in range(len(l)-n+1)]
    return res
def character_n_gram(s,n):
    l=s.replace(" ","")
    res=[l[i:i+n]for i in range(len(l)-n+1)]
    return res
print(word_n_gram(s,2))
print(character_n_gram(s,2))