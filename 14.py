path=__file__
f=open(path+"/../"+"popular-names.txt")
r=f.readlines()
n=int(input())
for i in range(n):
    print(r[i])