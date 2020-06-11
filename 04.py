s="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
s=s.replace(",","").replace(".","")
one=set([1,5,6,7,8,9,15,16,19])
from collections import Counter
c=Counter()
for i,j in enumerate(s.split()):
    if i+1 in one:
        c[j[0]]=i+1
    else:
        c[j[:2]]+=i+1
print(c)
