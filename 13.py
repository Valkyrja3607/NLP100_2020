path=__file__
f=open(path+"/../"+"col1.txt")
col1=f.readlines()
f=open(path+"/../"+"col2.txt")
col2=f.readlines()
res=""
for i,j in zip(col1,col2):
    res+=i.replace("\n","")+"\t"+j
with open(path+"/../"+"merge.txt",mode='w') as f:
    f.write(res)


