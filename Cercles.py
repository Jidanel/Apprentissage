from tkinter import *
from random import *
def drawcircle():
    global x1,x2,y1,y2
    coul='white'
    x1=0
    y1=20
    x2=20
    y2=0
    "Tracé du cercle"
    can1.create_oval(x1,x2,y1,y2,width=2,fill=coul)
    x1=105
    y1=135
    x2=135
    y2=105
    can1.create_oval(x1,x2,y1,y2,width=2,fill=coul)
    x1=170
    y1=150
    x2=150
    y2=170
    can1.create_oval(x1,x2,y1,y2,width=2,fill=coul)
    x1=80
    y1=60
    x2=60
    y2=80
    can1.create_oval(x1,x2,y1,y2,width=2,fill=coul)
    x1=0
    y1=80
    x2=80
    y2=0
    can1.create_oval(x1,x2,y1,y2,width=2,fill=coul)
    
#Programme principal
#creation du widget principal
fen1=Tk()
#Creation des widgets esclaves
can1=Canvas(fen1,bg='dark grey',height=300,width=300)
can1.pack(side=RIGHT)
bou1=Button(fen1,text='QUITTER', command=fen1.destroy)
bou1.pack(side=BOTTOM)
bou2=Button(fen1,text='Tracer un cercle',command=drawcircle)
bou2.pack()
fen1.mainloop()  #demarrage du receptionnaire d'evenements
  #destruction/fermeture de la fenetre

