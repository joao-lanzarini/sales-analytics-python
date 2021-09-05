from random import randint
import pandas as pd

def generate_id():
    df = pd.read_csv('./inventory.csv')

    while True:
        random = randint(1000, 9999)
        check = True

        for id in df['ID']:
            if str(random) == id:
                check = False
                break

        if check:
            break

    return random

generate_id()