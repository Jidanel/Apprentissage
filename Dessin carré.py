from Dessins_tortue import *
up()    #relever le crayon
goto(-150,50)  #reculer en haut et à gauche
#dessiner 10 carrés rouges alignés
i=0
while (i<30):
    down()  #abaisser le crayon
    carre(25,'red') #tracer un carré
    up() #relever le crayon
    forward(30)   #avancer + loin de 30
    i=i+1
