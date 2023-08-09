#*-* coding:Latin-1 -*-
import math

i=0
j=0
while(i<20):
    k=7*j
    print(k, end=" ")
    if(k%3==0):
        print("*", end=" ")
    j=j+1
    i=i+1
