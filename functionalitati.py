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
        lista_elemente: list = element.split(' ')
        lista_provizorie: list = []
        for _ in range(4):
            new_elem: str = random.choice(lista_elemente)
            while new_elem == lista_elemente[0] or new_elem == lista_elemente[-1] or new_elem in lista_provizorie:
                new_elem: str = random.choice(lista_elemente)
            lista_provizorie.append(new_elem)
            indexul = lista_elemente.index(new_elem)
            lista_elemente.pop(indexul)
            new_elem += '\n'
            lista_elemente.insert(indexul, new_elem)
        element = ' '.join(lista_elemente)
        print('\n' in element)
        return element
    else:
        return element
