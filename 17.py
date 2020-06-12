path=__file__
f=open(path+"/../"+"popular-names.txt")
import numpy as np
l=np.array([i.split("\t") for i in f.readlines()])
n=len(set("\n".join(l[:,0])))
print(n)