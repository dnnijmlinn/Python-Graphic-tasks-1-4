from datetime import datetime
from tkinter import *
from tkinter import filedialog, messagebox, simpledialog
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import *

ikkuna = Tk()
ikkuna.title('Muistio Pythonilla toteutettuna')
ikkuna.resizable(0, 0)  # type: ignore

notepad = ScrolledText(ikkuna, width = 100, height = 35)
tiedostonimi = ''



def cmdUusi():
    global tiedostonimi

    if len(notepad.get('1.0', END + '-1c'))>0:
        if messagebox.askyesno("Muistio", "Haluatko tallentaa muutokset?"):
            cmdTallenna()   # type: ignore
        else:
            notepad.delete(0.0, END)
    ikkuna.title("Muistio")




def cmdAvaa():
    fd = filedialog.askopenfile(parent = ikkuna, mode = 'r')
    t = fd.read()
    notepad.delete(0.0, END)
    notepad.insert(0.0, t)

def cmdTallenna():
    fd = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt')
    if fd!= None:
        data = notepad.get('1.0', END)
    try:
        fd.write(data)
    except:
        messagebox.showerror(title = "Virhe", message = "Tallentaminen ei onnistunut!")

def cmdTallennanimella():
    fd = filedialog.asksaveasfile(mode="w", defaultextension = ".txt")
    t = notepad.get(0,0, END)
    try:
        fd.write(t.rstrip())
    except:
        messagebox.showerror(title="Virhe", message="Tallentaminen ei onnistunut!")

def cmdLopeta():
    if messagebox.askyesno("Muistio", "Haluatko lopettaa?"):
        ikkuna.destroy()

def cmdLeikka():
    notepad.event_generate("<<Cut>>")

def cmdKopioi():
    notepad.event_generate("<<Copy>>")

def cmdLiita():
    notepad.event_generate("<<Paste>>")

def cmdTyhjenna():
    notepad.event_generate("<<Clear>>")

def cmdEtsi():
    notepad.tag_remove("Found",'1.9', END)
    find = simpledialog.askstring("Etsi", "Mitä haluat etsiä:")
    if find:
        idx = '1.0' #idx tarkoittaa indexiä
    while 1:
        idx = notepad.search(find, idx, nocase = 1, stopindex = END)

        if not idx:
            break
        lastidx = '%s+%dc' %(idx, len(find))
        notepad.tag_add('Löytyi:', idx, lastidx)
        idx = lastidx
    notepad.tag_config('Löytyi:', foreground = 'white', background = 'blue')
    notepad.bind("<1>", click)

def click(event):
    notepad.tag_config('Löytyi:',background='white',foreground='black')

def cmdValitsekaikki():
    notepad.event_generate("<<SelectAll>>")

def cmdTimeDate():
    now = datetime.now()
    # dd/mm/YY H:M:s
    dtString = now.strftime("%d/%m/%Y %H:%M:%S")
    label = messagebox.showinfo("Aika/päiväys", dtString)

def cmdOhje():
    label = messagebox.showinfo("Yleistä", "Muistio")

#Muistion valikot
muistioValikko = Menu(ikkuna)
ikkuna.configure(menu=muistioValikko)

#Tiedosto-valikko
tiedostoValikko = Menu(muistioValikko, tearoff = False)
muistioValikko.add_cascade(label='Tiedosto', menu = tiedostoValikko)

#alavalikoiden lisääminen
tiedostoValikko.add_command(label='Uusi', command = cmdUusi)
tiedostoValikko.add_command(label='Avaa...', command = cmdAvaa)
tiedostoValikko.add_command(label='Tallenna', command = cmdTallenna)
tiedostoValikko.add_command(label='Tallenna nimellä...', command = cmdTallennanimella)
tiedostoValikko.add_separator()
tiedostoValikko.add_command(label='Lopeta', command = cmdLopeta)

#Muokkaa valikko
muokkaaMenu = Menu(muistioValikko, tearoff = False)
muistioValikko.add_cascade(label='Muokkaa', menu = muokkaaMenu)

#alavalikot
muokkaaMenu.add_command(label='Leikkaa', command = cmdLeikka)
muokkaaMenu.add_command(label='Kopioi', command = cmdKopioi)
muokkaaMenu.add_command(label='Liitä', command = cmdLiita)
muokkaaMenu.add_command(label='Poista', command = cmdTyhjenna)
muokkaaMenu.add_separator()
muokkaaMenu.add_command(label='Etsi...', command = cmdEtsi)
muokkaaMenu.add_separator() #erotinviiva valikkoon
muokkaaMenu.add_command(label='Valitse kaikki', command = cmdValitsekaikki)
muokkaaMenu.add_command(label='Time/Date', command = cmdTimeDate)

#ohjevalikko
ohjeValikko = Menu(muistioValikko, tearoff = False)
muistioValikko.add_cascade(label='Ohje', menu = ohjeValikko)

#Yleistä-valikko 
ohjeValikko.add_command(label='Yleistä', command = cmdOhje)

notepad.pack()
ikkuna.mainloop()