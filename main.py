import time

import pandas as pd
from tkinter import *
from functionalitati import preluare_api, generare_question, data
import random
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
canvas.grid(column=0, row=0, columnspan=2)

but_true = Button(text='✅', bg=BUT_TRUE, font=('Bolt', 50), highlightthickness=0)
but_true.grid(column=0, row=1)

but_false = Button(text='❌', bg=BUT_FALSE, font=('Bolt', 50), highlightthickness=0)
but_false.grid(column=1, row=1)


def but_adevarat():
    print(f'din buton: {intrebarea_gen in data.intrebarea.to_list()}')
    time.sleep(1)
    joc()

def joc():
    global intrebarea_gen
    intrebarea_gen = generare_question()
    canvas.itemconfig(textul, text=intrebarea_gen)
    but_true.config(command=but_adevarat)


joc()
ecran.mainloop()
