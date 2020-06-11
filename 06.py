def character_n_gram(s,n):
    l=s.replace(" ","")
    res=[l[i:i+n]for i in range(len(l)-n+1)]
    return res
s="paraparaparadise"
t="paragraph"
x=set(character_n_gram(s,2))
y=set(character_n_gram(t,2))

#union
print(x|y)
#intersection
print(x^y)
#subtraction
print(x-y)

if "se" in x:
    print("se in x")
else:
    print("se not in x")
if "se" in y:
    print("se in y")
else:
    print("se not in y")