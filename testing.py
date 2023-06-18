# from datetime import datetime
#
# an = datetime.now().year
# luna = datetime.now().month
# zi = datetime.now().day
# ora = datetime.now().hour
# minute = datetime.now().minute
#
# with open('./work_log.txt', 'r') as fisier:
#     lista: list = fisier.readlines()
#
# element = lista[0].split(' ')
# element[1]: str = element[1].replace(element[1], f'{zi}/{luna}/{an}')
# element[-1]: str = element[-1].replace(element[-1], f'{ora}:{minute}\n')
# all_elem = ' '.join(element)
# lista.append(all_elem)
# with open('./work_log.txt', 'a') as fisier1:
#     fisier1.writelines(lista[-1])

from datetime import datetime

minut = datetime.now().minute
ora = datetime.now().hour
zi = datetime.now().day
luna = datetime.now().month
an = datetime.now().year

with open('./work_log.txt', 'r') as file:
    lista = file.readlines()
element: str = lista[-1]

element = element.replace('12', f'{zi}')
element = element.replace('6', f'{luna}')
element = element.replace('2023', f'{an}')
element = element.replace('20', f'{ora}')
element = element.replace('30', f'{minut}')

with open('./work_log.txt', 'a') as fisier:
    fisier.writelines(element + '\n')


