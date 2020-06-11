import random
s="I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
res=[]
for i in s.split():
    if len(i)<5:
        res.append(i)
    else:
        l=list(i[1:-1])
        random.shuffle(l)
        res.append(i[0]+"".join(l)+i[-1])
print(" ".join(res))