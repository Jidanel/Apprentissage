#*-* coding:Latin-1 -*-
import math
t1=[31,28,31,30,31,30,31,31,30,31,30,31]
t1=list(t1)
t2=['Janvier','Fevrier','Mars','Avril','Mai','Juin','Juillet','Aout','Septembre','Octobre','Novembre','Decembre']
t2=list(t2)
i=0
t3=[]  #on declare la liste t3
t4=""
while(i<len(t1)):       #tant que i<taille de t1
      t3.append(t2[i])   #on ajoute le premier element de t2 dans t3
      t3.append(t1[i])   #on ajoute le premier element de t1. On construit la liste petit à petit
      i=i+1
print(t3)
t4=str(t2)
print(t4)

