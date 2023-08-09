from tkinter import *
def rond(event):
    x=event.x
    y=event.y
    canv.create_oval(x-5,y-5,x+5,y+5,fill="red")
    chaine1.configure(text= "clic detecté en X= " +str(event.x))
    chaine2.configure(text= " Y= "+str(event.y))
    canv.

fen=Tk()
canv=Canvas(fen,width=200, height=150, bg="light yellow")
canv.bind("<Button-1>", rond)
canv.pack()
chaine1 = Label(fen)
chaine2 = Label(fen)
chaine1.pack()
chaine2.pack()
fen.mainloop()
