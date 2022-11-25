from tkinter import Button, DoubleVar, Entry, IntVar, Label, Tk, W


def Laskeyhteen():
    yhteensa = DoubleVar()
    yhteensa = round(ekanumero.get()+tokanumero.get(),2)
    vastaus.config(text="Yhteensä: "+str(yhteensa))
ikkuna = Tk()
ikkuna.title("Kahden luvun yhteenlaskeminen")

#
ikkuna.geometry("400x200")

#
Label(ikkuna, text="Annatko ensimäinen numeron:").grid(row=0, sticky=W)
Label(ikkuna, text="Annatko toisen numeron:").grid(row=1, sticky=W)
#
ekanumero = DoubleVar()
tokanumero = DoubleVar()

luku1 = Entry(ikkuna, textvariable=ekanumero).grid(row=0, column=1)
luku21 = Entry(ikkuna, textvariable=tokanumero).grid(row=1, column=1)

laskenappi = Button(ikkuna, text="Laske yhteen", command=Laskeyhteen).grid(row=2, column=1)
vastaus = Label(ikkuna)
vastaus.grid(row=3, column=1)

ikkuna.mainloop()