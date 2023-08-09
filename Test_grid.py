from tkinter import *
#Creation de la fenêtre
fen = Tk()
#Creation des labels et champs de saisie
text1=Label(fen,text="Premier choix")
text2=Label(fen,text="Deuxieme choix")
text3=Label(fen,text="Troisième choix")
entr1=Entry(fen)
entr2=Entry(fen)
entr3=Entry(fen)
#creation d'un widget
can=Canvas(fen,width=160, height=160, bg="white")
#photo=PhotoImage(file='C:\Users\Jidanel\Desktop\Mutations\tr.gif')
#item=can.creaate_image(100,100,image=photo)
#mise en pahe à l'aide de gride()
text1.grid(row=1, sticky=E)
text2.grid(row=2, sticky=E)
text3.grid(row=3, sticky=E)
entr1.grid(row=1, column=2)
entr2.grid(row=2, column=2)
entr3.grid(row=3, column=2)
#can.grid(row=1, column=3, rowspan=3, padx=10, pady=5)
#demarrage de la fenetre en boucle
fen.mainloop()