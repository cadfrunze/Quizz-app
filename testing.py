from datetime import datetime

with open('./work_log.txt', 'a') as fisier:
    fisier.writelines(f'Data: {datetime.now().day}/{datetime.now().month}/{datetime.now().year} | Ora: {datetime.now().hour}:{datetime.now().minute}\n')
import pandas

data_dict = {
    "students": ["Maryus", "Iulia", "Sebi"],
    "skill": [10, 20, 30]
}

data1 = pandas.DataFrame(data_dict)
data1.to_csv("testing", index=False)
new_data = pandas.read_csv('testing')
new_data1 = new_data[new_data.students == 'Iulia']
print(new_data1)