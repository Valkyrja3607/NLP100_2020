path=__file__
f=open(path+"/../"+"popular-names.txt")
import numpy as np
l=np.array([i.split("\t") for i in f.readlines()])
col1="\n".join(l[:,0])
col2="\n".join(l[:,1])
with open(path+"/../"+"col1.txt",mode='w') as f:
    f.write(col1)
with open(path+"/../"+"col2.txt",mode='w') as f:
    f.write(col2)