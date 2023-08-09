from turtle import *
def carre(taille,couleur):
    "fonction qui dessine un carré de taille et de couleur determinée"
    color(couleur)
    c=0
    while(c<4):           #c<4 cest pour les 4 cotés du carré donc cette boucle dessine exactement un carré
        forward(taille)   #on avance de taille
        right(90)   #On prend un angle de 90 degré suivant la droite (ici en descendant)
        c=c+1              #on passe au coté suivant
