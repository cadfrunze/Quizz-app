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