#*-* coding:Latin-1 -*-
from math import *
t=["papa","maman","ecolier","patate","cuisine","Pasteur","Maximilien","Torche","Sel"]
t2=[]
t3=[]
c=0
i=0
i=int(i)#initialisation du compteur
k=len(t)   #calcul de la taille de laliste
while(i<k):
    if(len(t[i])>6): #on teste la valeur de la position i est paire
       t2.append(t[i])   #si oui on l'ajoute à la liste t2
    else:
         t3.append(t[i])#sinon si cest impair on ajoute à t3
    i=i+1
print("la liste des mots superieurs à 6 lettres: ",t3)
print("la liste des mots inferieurs à 6 lettres est ",t2)
