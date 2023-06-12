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


test = 'maryaaus'
print(test)
new_index = test.index(test[1])
test = test.replace(test[new_index], 'b')
print(test)