import tkinter as tk
from tkinter import *

from fpdf import FPDF


def Pizzakoonvalinta():
    selection = koko.get()
    return selection
    label.config(text = selection)

def header(self):
    self.set_font('Arial', 'B', 15)
    self.cell(80)
    self.cell(30, 10, 'Title', 1, 0, 'C')
    self.ln(20)


def footer(self):
    self.set_y(-15)
    self.set_font('Arial', 'I', 8)
    self.cell(0, 10, 'Page', + str(self.page_no()) + '/{nb}', 0, 0, 'C')

def Tulostakuitti():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.image('blank-frame-italy-insignia-book-cover-background-template-58713926.jpeg', x = 0, y = 0, w = 210, h = 297, type = '', link = '')
    pdf.cell(70)
    pdf.cell(50, 20, 'Italialainen pizzeria')
    #
    pizzarivit = tilaus.get('1.0', 'end').split('\n')
    #
    rivimaara = int(tilaus.index('end').split('.')[0])-1
    pdf.ln(60)
    pdf.cell(48)
    for i in range(0, rivimaara):
        pdf.cell(50, 10, pizzarivit[i], 0, 2)
    pdf.output('/Users/denisbogdanov/Desktop/Denis/Projects/Python/opi.riveria/kuitti.pdf')

def Laskepizzanhinta():
    phinta = DoubleVar()
    if(koko.get()==1): phinta = 5
    else: phinta = 9

    if(kinkku.get()==1): phinta = phinta + 0.75
    if(ananas.get()==1): phinta = phinta + 0.50
    if(meetwursi.get()==1): phinta = phinta + 0.50
    if(kana.get()==1): phinta = phinta + 0.50
    if(herkkusieni.get()==1): phinta = phinta + 0.50
    if(aurajuusto.get()==1): phinta = phinta + 0.50

    if(maksutapa.get()==3): phinta = round(phinta * 0.9,2)
    if(maksutapa.get()==4): phinta = round(phinta * 1.05,2)
    else: phinta = phinta

    hinta.set(phinta)
    ph.config(state=DISABLED)
    
def Laskeyhteensa():
    if tilaus.compare("end-1c", "==", "1.0"):
        tilaus.insert(END, "Määrä: " + str(maara.get()) + " Hinta: " + str(hinta.get()) + " Yhteensä: " + str(maara.get()*hinta.get()))
    else: 
        #tilaus.insert(END, '/n')
        tilaus.insert(END, "\nMäärä: " + str(maara.get()) + " Hinta: " + str(hinta.get()) + " Yhteensä: " + str(maara.get()*hinta.get()))

ikkuna = Tk()
ikkuna.title("Pizzalaskuri käyttöliittymän toteutus")
#
ikkuna.geometry("700x700")

Label(ikkuna, text="Lasken pizzan hinnan ja tilauksen loppusumman huomioiden tilausmäärän ja a'-hinnan:").grid(row=0, column=0)

koko = Label(ikkuna, text="Valitse pizzan koko:").grid(row=1, column=0, sticky="W")
#
koko = IntVar()

r1 = Radiobutton(ikkuna, text="Normaali 5 eur",
            variable=koko, command=Laskepizzanhinta, value=1).grid(row=3, column=0, sticky="W")

r2 = Radiobutton(ikkuna, text="Perhe 9 eur",
            variable=koko, command=Laskepizzanhinta, value=2).grid(row=4, column=0, sticky="W")




taytteet = Label(ikkuna, text="Valitse täytteet").grid(row=5, column=0, sticky="W")
#checkbutton
kinkku = IntVar()
chckb = Checkbutton(ikkuna, text="Kinkku +0,75 eur", command=Laskepizzanhinta, variable=kinkku,onvalue=1).grid(row=6, column=0, sticky="W")

ananas = IntVar()
chckb = Checkbutton(ikkuna, text="Ananas +0,50 eur", command=Laskepizzanhinta, variable=ananas,onvalue=1).grid(row=7, column=0, sticky="W")

meetwursi = IntVar()
chckb = Checkbutton(ikkuna, text="Meetwursi +0,50 eur", command=Laskepizzanhinta, variable=meetwursi,onvalue=1).grid(row=8, column=0, sticky="W")


kana = IntVar()
chckb = Checkbutton(ikkuna, text="Kana +0,50 eur", command=Laskepizzanhinta, variable=kana,onvalue=1).grid(row=9, column=0, sticky="W")

herkkusieni = IntVar()
chckb = Checkbutton(ikkuna, text="Herkkusieni +0,50 eur", command=Laskepizzanhinta, variable=herkkusieni,onvalue=1).grid(row=10, column=0, sticky="W")

aurajuusto = IntVar()
chckb = Checkbutton(ikkuna, text="Aurajuusto +0,50 eur", command=Laskepizzanhinta, variable=aurajuusto,onvalue=1).grid(row=11, column=0, sticky="W")

Label(ikkuna, text=" ").grid(row=13, column=0, sticky="W")
Label(ikkuna, text="Maksutapa:").grid(row=14, column=0, sticky="W")
maksutapa = IntVar()

r3 = Radiobutton(ikkuna, text="käteinen - 10 %",
            variable=maksutapa, command=Laskepizzanhinta, value=3).grid(row=15, column=0, sticky="W")

r4 = Radiobutton(ikkuna, text="pankkikortti + 5 %",
            variable=maksutapa, command=Laskepizzanhinta, value=4).grid(row=16, column=0, sticky="W")
        
r5 = Radiobutton(ikkuna, text="VISA 0%",
            variable=maksutapa, command=Laskepizzanhinta, value=5).grid(row=17, column=0, sticky="W")

Label(ikkuna, text="Annatko pizzojen määrät:").grid(row=18, column=0, sticky="W")
Label(ikkuna, text="Pizzan hinta:").grid(row=19, column=0, sticky="W")

maara = IntVar()
hinta = DoubleVar()

#luodaan syöttökentät
pizzojenmaara = Entry(ikkuna, justify=LEFT, textvariable=maara)
pizzojenmaara.grid(row=18, column=0)
#pizzojen oletusmäärä 1
maara.set(1)

ph = Entry(ikkuna, textvariable=hinta)
ph.grid(row=19, column=0)
ph.config(state="disabled")

#Laskenappi
laskenappi = Button(ikkuna, text="Tilaa pizza", command=Laskeyhteensa).grid(row=20, column=0, sticky="W")
tulostanappi = Button(ikkuna, text="Tulosta kuitti", command=Tulostakuitti).grid(row=20, column=1, sticky="W")




kassakuitti = Label(ikkuna, text="Kassakuitti")
kassakuitti.grid(row=25, sticky="W")

tilaus = Text(ikkuna, height = 10, width=50)
tilaus.grid(row=27, sticky="W")

ikkuna.mainloop()