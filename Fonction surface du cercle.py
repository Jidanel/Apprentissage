#*-* coding:Latin-1 -*-
from math import *

def carre(x):
    l=x*x
    return l

def surfCercle(r):
    c=carre(r)*3.14
    print("la surface du cercle est :",c)
b=input("Entrez la valeur du rayon: ")
b=float(b)
print(surfCercle(b))

