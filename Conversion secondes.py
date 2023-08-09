#*-* coding:Latin-1 -*-
import math
n=60000
x=n/31622400
a=math.floor(x)  #Nombres d'années
b=(x-a)*31622400  #on recupere la partie decimale * par le diviseur pour la suite

c=b/2592000
d=math.floor(c)  #Nombres de mois
e=(c-d)*2592000  #on recupere la partie decimale * par le diviseur pour la suite

f=e/86400        
g=math.floor(f)  #Nombres de jours
h=(f-g)*86400   #on recupere la partie decimale * par le diviseur pour la suite

i=h/3600
j=math.floor(i)  #Nombres d'heures
k=(i-j)*3600    #on recupere la partie decimale * par le diviseur pour la suite

l=k/60
m=math.floor(l)  #Nombres de minutes
o=(l-m)*60       #on recupere la partie decimale * par le diviseur pour la suite
p=math.floor(o)

print(n," secondes correspond à ",a," années",d," mois",g," jours",j," Heures",m," minutes",p," secondes")
