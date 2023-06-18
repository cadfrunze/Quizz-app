from tkinter import *
import pandas as pd
from functionalitati import generare_question, data, verificare_len
from datetime import datetime

# Valori pt GUI + metodele after si after_cancel
BG_COLOR = '#108A2A'
BUT_TRUE = '#10798A'
BUT_FALSE = '#8A2410'
FALSE_BG = '#FF3333'
TRUE_BG = '#10318A'
scor = 0
intrebarea_gen: None = None
intoarceri = None
intoarcere_cron = None
# Configurare GUI
ecran = Tk()
ecran.title('Quizz Game')
ecran.resizable(False, False)
ecran.config(padx=2, pady=2, bg=BG_COLOR)

canvas = Canvas(width=600, height=600, bg=BG_COLOR, highlightthickness=0)
textul = canvas.create_text(300, 150, text='', font=('italic', 10))
scorul = canvas.create_text(100, 50, text='', fill='orange')
cron_text = canvas.create_text(300, 50, text='', fill='orange')
canvas.grid(column=0, row=0, columnspan=2)

but_true = Button(text='✅', bg=BUT_TRUE, font=('Bolt', 50), highlightthickness=0)
but_true.grid(column=0, row=1)

but_false = Button(text='❌', bg=BUT_FALSE, font=('Bolt', 50), highlightthickness=0)
but_false.grid(column=1, row=1)


# Cronometru
def cronometrul(count: int):
    global intoarcere_cron
    """Functie cronometrare timp"""
    if count >= 10:
        canvas.itemconfig(cron_text, text=f'{count}', fill='blue', font=('normal', 10))
    elif 9 >= count >= 6:
        canvas.itemconfig(cron_text, text=f'{count}', fill='orange', font=('normal', 20))
    elif count <= 5:
        canvas.itemconfig(cron_text, text=f'{count}', fill='red', font=('normal', 50))
    intoarcere_cron = ecran.after(1000, cronometrul, count - 1)
    if count == 0:
        culori(False, 3)


# Functie pt anulare functii de la butoane
def pass_command():
    """Functie pt butoane, anulare comenzi"""
    pass


# Functii pt schimbare/refresh BG
def bg_colors():
    """BG Color"""
    canvas.config(bg=BG_COLOR)
    ecran.config(bg=BG_COLOR)


def culori(boolean: bool, incercari: int):
    """1. Vai de pula mea cat m-am chinuit!....metoda asta after mi-o dat in cap.
    2. Deci mi-a luat jumatate de zi la refreshul de la bg sa imi dau seama pot sa mai adaug o metoda after...
    ca sa dea refresh"""
    global intoarceri, intoarcere_cron
    ecran.after_cancel(intoarcere_cron)
    ecran.after(500, bg_colors)
    but_true.config(command=pass_command)
    but_false.config(command=pass_command)
    if boolean is True:
        canvas.config(bg=TRUE_BG)
        ecran.config(bg=TRUE_BG)
    else:
        canvas.config(bg=FALSE_BG)
        ecran.config(bg=FALSE_BG)
    if incercari > 0:
        intoarceri = ecran.after(1000, culori, boolean, incercari - 1)
    elif incercari == 0:
        canvas.config(bg=BG_COLOR)
        ecran.config(bg=BG_COLOR)
        ecran.after_cancel(intoarceri)
        joc()


# Functii pt butoane + verificare raspuns
def but_adevarat():
    global scor, intoarceri
    verificare = data[data.intrebarea == intrebarea_gen]
    raspuns: bool = verificare.adevarat.item()
    if raspuns is True:
        scor += 1
        culori(raspuns, 3)
    else:
        culori(raspuns, 3)


def but_fals():
    global scor, intoarceri
    verificare = data[data.intrebarea == intrebarea_gen]
    raspuns: bool = verificare.adevarat.item()
    if raspuns is False:
        scor += 1
        culori(True, 3)

    else:
        culori(False, 3)


# Rulare joc
def joc():
    global intrebarea_gen, scor
    if scor >= 1:
        canvas.itemconfig(scorul, text=f'Scor: {scor}')
    intrebarea_gen = generare_question()
    verrificare_continut = verificare_len(intrebarea_gen)
    canvas.itemconfig(textul, text=verrificare_continut)
    but_true.config(command=but_adevarat)
    but_false.config(command=but_fals)
    cronometrul(30)


if '__main__' == __name__:
    joc()
    ecran.mainloop()
SECUNDE = datetime.now().second
MINUT: int = datetime.now().minute
ORA: int = datetime.now().hour
ZIUA: int = datetime.now().day
LUNA: int = datetime.now().month
AN: int = datetime.now().year
DATA_SAVE: str = f'{ZIUA}/{LUNA}/{AN}'
ORA_SAVE: str = f'{ORA}:{MINUT}:{SECUNDE}'
ora_list: list = []
data_list: list = []
scor_list: list = []
try:
    file = pd.read_csv('./log_testing.csv')

except FileNotFoundError:
    log_data_dict: dict = {
        'data': DATA_SAVE,
        'ora': ORA_SAVE,
        'scor': scor
    }
    data_ = pd.DataFrame(index=['Series'], data=log_data_dict)
    data_.to_csv('./log_testing.csv', index=False)
else:
    data_dict = pd.read_csv('./log_testing.csv')
    log_data_dict: dict = data_dict.to_dict('list')
    log_data_dict['data'].append(DATA_SAVE)
    log_data_dict['ora'].append(ORA_SAVE)
    log_data_dict['scor'].append(scor)
    data_save = pd.DataFrame(log_data_dict)
    data_save.to_csv('./log_testing.csv', index=False)
