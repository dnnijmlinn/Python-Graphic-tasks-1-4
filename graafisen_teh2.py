from tkinter import (NW, Button, DoubleVar, Entry, IntVar, Label, Radiobutton,
                     Tk, W, messagebox)


def Laskeyhteen():
    yhteensa = DoubleVar()
    yhteensa = round(maarat.get() * hinnan.get())

    if maarat.get() > 0:
        if var.get() == 0:
            yhteensa = yhteensa + ((yhteensa/100)*3)
            vastaus.config(text="Yhteensä: "+str(yhteensa))
            messagebox.showinfo("messagebox", format(yhteensa, ".2f"))
        elif var.get() ==1:
            yhteensa = yhteensa - ((yhteensa/100)*2)
            vastaus.config(text="Yhteensä: "+str(yhteensa))
            messagebox.showinfo("messagebox", format(yhteensa, ".2f"))
        elif var.get() ==2:
            yhteensa = yhteensa - ((yhteensa/100)*4)
            vastaus.config(text="Yhteensä: "+str(yhteensa))
            messagebox.showinfo("messagebox", format(yhteensa, ".2f"))

    else :
        vastaus.config(text="On oltava positiivinen luku määrässä")
        messagebox.showinfo("messagebox", format("On oltava positiivinen luku määrässä"))
    
    

ikkuna = Tk()
ikkuna.title("Kahden luvun yhteenlaskeminen")

#
ikkuna.geometry("750x400")

#
Label(ikkuna, text="Lasken tilauksen loppusumman huomioiden tilausmäärän, a'hinnan ja maksutavan:").grid(row=0, column=0)
Label(ikkuna, text="Annatko ostettavan tuotteen määrät:").grid(row=1, column=0)
Label(ikkuna, text="Annatko ostettavan tuotteen hinnan:").grid(row=2, column=0)
#
maarat = DoubleVar()
hinnan = DoubleVar()

luku1 = Entry(ikkuna, textvariable=maarat).grid(row=1, column=1)
luku21 = Entry(ikkuna, textvariable=hinnan).grid(row=2, column=1)

laskenappi = Button(ikkuna, text="Laske yhteen!", command=Laskeyhteen).grid(row=8, column=1)
vastaus = Label(ikkuna)
vastaus.grid(row=9, column=1)

################################################################    

var = IntVar()
var.set(0)
r1 = Radiobutton(text="Käteinen + 3% lisää hintaa",
            variable=var, value=0).grid(row=3, column=0, sticky="W")
r2 = Radiobutton(text="VISA - 2% alennus",
            variable=var, value=1).grid(row=4, column=0, sticky="W")
r3 = Radiobutton(text="OP tilisiirto -4%", 
            variable=var, value=2).grid(row=5, column=0, sticky="W")

label = Label(width=20, height=2)
label.grid(row=5, column=0, columnspan=2)

ikkuna.mainloop()