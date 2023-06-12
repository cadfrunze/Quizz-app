from datetime import datetime

an = datetime.now().year
luna = datetime.now().month
zi = datetime.now().day
ora = datetime.now().hour
minute = datetime.now().minute

with open('./work_log.txt', 'r') as fisier:
    lista = fisier.readlines()

print(lista)