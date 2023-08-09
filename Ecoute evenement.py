from tkinter import *
def pointeur(event):
    chaine1.configure(text= "clic detecté en X= " +str(event.x))
    chaine2.configure(text= " Y= "+str(event.y))

fen=Tk()
cadre=Frame(fen,width=200, height=150, bg="light yellow")
cadre.bind("<Button-1>", pointeur)
cadre.pack()
chaine1 = Label(fen)
chaine2 = Label(fen)
chaine1.pack()
chaine2.pack()
fen.mainloop()
