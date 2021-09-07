import pandas as pd
from random import randint

def generate_id():

    try:
        df = pd.read_csv('./purchases.csv')

    except FileNotFoundError:
        print('File not found.')
        
    else:

        while True:
            random = randint(100000, 999999)
            check = True

            for id in df['ID']:
                if str(random) == id:
                    check = False
                    break

            if check:
                break

        return random