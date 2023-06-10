import pandas as pd
from tkinter import *
from functionalitati import preluare_api, generare_question
import random
preluare_api()
BG_COLOR = '#108A2A'
BUT_TRUE = '#10798A'
BUT_FALSE = '#8A2410'
FALSE_BG = '#FF3333'
TRUE_BG = '#10318A'
scor = 0
intrebarea_gen: None = None

data_brut = pd.read_csv('./data/data.csv')

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


def but_adevarat():
    print(intrebarea_gen)
    data1 = data_brut[data_brut.intrebarea == intrebarea_gen]
    print(data1)


def joc():
    global intrebarea_gen
    intrebarea_gen = generare_question()
    print(intrebarea_gen)
    canvas.create_text(300, 150, text=intrebarea_gen, font=('italic', 10))
    but_true.config(command=but_adevarat)


joc()
ecran.mainloop()
