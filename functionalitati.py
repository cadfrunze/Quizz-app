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
    return intrebarea


def verificare_len(element: str) -> str:
    if len(element) >= 87:
        index_list: list = []
        index_list_prov: list = []
        for elem in range(len(element)-1):
            if element[elem] == ' ':
                index_list.append(elem)
        index_list.pop(0)
        index_list.pop(-1)
        for _ in range(4):
            new_elem: int = random.choice(index_list)
            while new_elem in index_list_prov:
                new_elem: int = random.choice(index_list)
            print(new_elem)
            element = element[new_elem].replace(element[new_elem], '\n')
        print('\n' in element)
        return element
    else:
        return element






