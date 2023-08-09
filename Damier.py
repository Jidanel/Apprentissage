from tkinter import *
from random import *
def drawdamier():
    global x1,x2,y1,y2
    coul='blue'
    x1=0
    y1=0
    x2=20
    y2=20
    while(x1<=200):
         while(y1<=200):
            "Tracé du rectangle"
            can1.create_rectangle(x1,y1,x2,y2,width=1,fill=coul)
            y1=y1+10
            y2=y2+10
    x1=x1+10
    x2=x2+10
        

#Programme principal
#creation du widget principal
fen1=Tk()
#Creation des widgets esclaves
can1=Canvas(fen1,bg='white',height=600,width=600)
can1.pack(side=LEFT)
bou1=Button(fen1,text='QUITTER', command=fen1.destroy)
bou1.pack(side=BOTTOM)
bou2=Button(fen1,text='damier',command=drawdamier)
bou2.pack()

fen1.mainloop()  #demarrage du receptionnaire d'evenements
  #destruction/fermeture de la fenetre

