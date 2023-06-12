import time
from tkinter import *
from functionalitati import preluare_api, generare_question, data, verificare_len

preluare_api()
BG_COLOR = '#108A2A'
BUT_TRUE = '#10798A'
BUT_FALSE = '#8A2410'
FALSE_BG = '#FF3333'
TRUE_BG = '#10318A'
scor = 0
intrebarea_gen: None = None

ecran = Tk()
ecran.title('Quizz Game')
ecran.resizable(False, False)
ecran.config(padx=2, pady=2, bg=BG_COLOR)

canvas = Canvas(width=600, height=600, bg=BG_COLOR, highlightthickness=0)
textul = canvas.create_text(300, 150, text='', font=('italic', 10))
scorul = canvas.create_text(100, 50, text='', fill='blue')
canvas.grid(column=0, row=0, columnspan=2)

but_true = Button(text='✅', bg=BUT_TRUE, font=('Bolt', 50), highlightthickness=0)
but_true.grid(column=0, row=1)

but_false = Button(text='❌', bg=BUT_FALSE, font=('Bolt', 50), highlightthickness=0)
but_false.grid(column=1, row=1)


def but_adevarat():
    global scor
    verificare = data[data.intrebarea == intrebarea_gen]
    raspuns: bool = verificare.adevarat.item()
    if raspuns is True:
        scor += 1
    time.sleep(1)
    joc()


def but_fals():
    global scor
    verificare = data[data.intrebarea == intrebarea_gen]
    raspuns: bool = verificare.adevarat.item()
    if raspuns is False:
        scor += 1
    time.sleep(1)
    joc()


def joc():
    global intrebarea_gen, scor
    if scor >= 1:
        canvas.itemconfig(scorul, text=f'Scor: {scor}')
    intrebarea_gen = generare_question()
    verrificare_continut = verificare_len(intrebarea_gen)
    canvas.itemconfig(textul, text=verrificare_continut)
    but_true.config(command=but_adevarat)
    but_false.config(command=but_fals)


joc()
ecran.mainloop()

# if '__main__' == __name__:
#     joc()
