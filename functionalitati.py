import requests
import pandas as pd
import random


def preluare_api():
    """Functie preluare date API + convertire in format .csv (./data/data.csv)"""
    raspuns = requests.get('https://opentdb.com/api.php?amount=50&type=boolean')
    raspuns.raise_for_status()
    data = raspuns.json()
    list_data = [elem for elem in data['results']]
    intrebari_data = [elem1['question'] for elem1 in list_data]
    true_data = [elem3['correct_answer'] for elem3 in list_data]
    false_data = [''.join(elem4['incorrect_answers']) for elem4 in list_data]
    data_dict = {
        'intrebarea': intrebari_data,
        'adevarat': true_data,
        'fals': false_data
    }
    data_csv = pd.DataFrame(data_dict)
    data_csv.to_csv('./data/data.csv', index=False)


data = pd.read_csv('./data/data.csv')
intrebarile = data.intrebarea
intrebarea_list: list = intrebarile.to_list()


def generare_question() -> str:
    intrebarea: str = random.choice(intrebarea_list)
    intrebarea_list.remove(intrebarea)
    print(intrebarea in data.intrebarea.to_list())
    return intrebarea


def verificare_len(element: str) -> str:
    if len(element) >= 87:
        list_element: list = element.split(' ')
        dubluri: list = []
        for _ in range(3):
            elem: str = random.choice(list_element)
            while elem in dubluri:
                elem: str = random.choice(list_element)
            dubluri.append(elem)
            count = list_element.count(elem)
            elem1 = elem + '\n'
            list_element.pop(count)
            list_element.insert(count, elem1)
        elem_final: str = ' '.join(list_element)
        return elem_final
    else:
        return element






