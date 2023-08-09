#*-* coding:Latin-1 -*-
import math
t=[32,20,14,255,23,69,78,74,100]
t2=[]
c=0
i=0
i=int(i)#initialisation du compteur
k=len(t)   #calcul de la taille de laliste
while(i<k):
    if(t[i]>t[0]): #on teste la valeur de la position i avec celle de la position 0
       c=t[i]
       t[i]=t[0]   #Si cette valeur est plus grande on permute avec t[0]
       t[0]=c
    else:
        i=i+1       #sinon on passe à la position suivante
        
print(t[0])  #On affiche le plus grand
