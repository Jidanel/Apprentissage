#*-* coding:Latin-1 -*-
import math from *
t=[32,20,14,255,23,69,78,74,100]
t2=[]
t3=[]
c=0
i=0
i=int(i)#initialisation du compteur
k=len(t)   #calcul de la taille de laliste
while(i<k):
    if(t[i]%2==0): #on teste la valeur de la position i est paire
       t2.append(t[i])   #si oui on l'ajoute à la liste t2
    else:
         t3.append(t[i])#sinon si cest impair on ajoute à t3
    i=i+1
print("la liste des nombres impairs est ",t3)
print("la liste des nombres impairs est ",t2)
