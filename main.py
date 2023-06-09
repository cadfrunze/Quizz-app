import pandas as pd
from tkinter import *
from functionalitati import *

BG_COLOR = '#108A2A'
BUT_TRUE = '#10798A'
BUT_FALSE = '#8A2410'
FALSE_BG = '#FF3333'
TRUE_BG = '#10318A'
scor = 0
intrebarea_str: str = generare_question()

preluare_api()

ecran = Tk()
ecran.title('Quizz Game')
ecran.resizable(False, False)
ecran.config(padx=2, pady=2, bg=BG_COLOR)

canvas = Canvas(width=600, height=600, bg=BG_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

but_true = Button(text='✅', bg=BUT_TRUE, font=('Bolt', 50), highlightthickness=0)
but_true.grid(column=0, row=1)

but_false = Button(text='❌', bg=BUT_FALSE, font=('Bolt', 50), highlightthickness=0)
but_false.grid(column=1, row=1)


def fals():
    return False


def adevarat():
    global scor
    if data[data.intrebarea == data.adevarat]:
        scor += 1
    continuare_joc()


def joc():
    global intrebarea_str
    intrebarea_str = generare_question()
    if len(intrebarea_str) >= 85:
        intrebarea = verificare_len(intrebarea_str)
    canvas.create_text(300, 150, text=intrebarea_str, font=('italic', 10))
    but_true.config(command=adevarat)

def continuare_joc():
    ecran.after(1000, joc)


joc()
ecran.mainloop()
