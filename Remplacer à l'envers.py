#*-* coding:Latin-1 -*-
import math
n="Je mange"
l=len(n)
k=list(n)
p=list(n)
l=len(n)
i=0
while(i<len(n)):
    k[i]=p[l-1]
    i=i+1
    l=l-1
s="".join(k)
print(s)
