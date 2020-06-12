path=__file__
f=open(path+"/../"+"popular-names.txt")
r=f.readlines()
n=int(input())
r=[r[i::n]for i in range(n)]

