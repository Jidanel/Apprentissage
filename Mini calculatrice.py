from tkinter import *
from math import *

#Definition de l'action à efectuer si l'utilisateur actionne la touche entrée
def evaluer(event):
    chaine.configure(text="Résultat =" +str(eval(entree.get())))

#Programme principal
fenetre = Tk()   #creation de la fenetre
entree=Entry(fenetre) #definition de la variable entree qui recupere l'entrée dans la fenetre
entree.bind("<Return>",evaluer) #Après avoir taper la touche entrée executer la commande evaluer
chaine = Label(fenetre)
entree.pack()
chaine.pack()
fenetre.mainloop()
