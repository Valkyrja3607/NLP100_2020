path=__file__
f=open(path+"/../"+"popular-names.txt")
l=f.readlines()
for s in l:
    s.replace("\t"," ")
    print(s)

