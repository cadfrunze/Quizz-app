import requests
import pandas as pd


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

