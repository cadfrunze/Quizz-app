import pandas as pd
from tkinter import *
from functionalitati import preluare_api
import random

BG_COLOR = '#108A2A'
BUT_TRUE = '#10798A'
BUT_FALSE = '#8A2410'
FALSE_BG = '#FF3333'
TRUE_BG = '#10318A'

preluare_api()
data = pd.read_csv('./data/data.csv')
intrebarile = data.intrebarea
intrebarea_list: list = intrebarile.to_list()

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


def verificare_len(element: str):
    count = element.count(' ')
    count -= 1
    add = random.randint(1, count)
    element = element[add] + '\n'
    return element


def joc():
    intrebarea: str = random.choice(intrebarea_list)
    intrebarea_list.remove(intrebarea)
    if len(intrebarea) >= 85:
        intrebarea = verificare_len(intrebarea)
    canvas.create_text(300, 150, text=intrebarea, font=('italic', 10))


joc()
ecran.mainloop()
