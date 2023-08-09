from tkinter import *
from random import *


#Definition des fonctions de gestionnaire d'evenements
def drawline():
    pal=[190,10,10,190]
    e=randrange(4)
    x1=pal[e]
    f=randrange(4)
    y1=pal[f]
    g=randrange(4)
    x2=pal[g]
    h=randrange(4)
    y2=pal[h]
    pal=['purple','cyan','maroon','green','red','blue','orange','yellow']
    c=randrange(8)
    coul=pal[c]
    "Tracé d'une ligne dans le canevas can1"
    can1.create_arc(x1,y1,x2,y2,width=2,fill=coul)
def drawline2():
    t1=100
    u1=100
    t2=100
    u2=100
    coul2='red'
    can1.create_line(t1,u1,t2,u2,width=2,fill=coul2)
    #modification des coordonnées
  
def changecolor():
    "Changement aleatoire de couleur du tracé"
    global coul
    pal=['purple','cyan','maroon','green','red','blue','orange','yellow']
    c=randrange(8)
    coul=pal[c]

#Programme principal
#les variables suivantes seront utilisées de facon global
    
    coul='dark green'   #couleur de la ligne
#creation du widget principal
fen1=Tk()
#Creation des widgets esclaves
can1=Canvas(fen1,bg='dark grey',height=200,width=200)
can1.pack(side=LEFT)
bou1=Button(fen1,text='QUITTER', command=fen1.destroy)
bou1.pack(side=BOTTOM)
bou2=Button(fen1,text='Tracer une ligne',command=drawline)
bou2.pack()
bou3=Button(fen1,text='Autre couleur',command=changecolor)
bou3.pack()
bou4=Button(fen1,text='viseur', command=drawline2)
bou4.pack()

fen1.mainloop()  #demarrage du receptionnaire d'evenements
  #destruction/fermeture de la fenetre
