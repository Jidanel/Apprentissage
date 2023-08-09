#*-* coding:Latin-1 -*-
import math
n="""Je vais au marché pour acheter de la nourriture"""
b=len(n)
i=0
p=0
while(i<b):
    if(n[i]=="e"):
        p=p+1
    i=i+1
if(p!=0):
    print("La chaine contient e et il apparait ",p," fois")
else:
    print("La chaine ne contient pas e")
