from random import randint
import pandas as pd

def generate_id():

    try:
        df = pd.read_csv('./inventory.csv')

    except FileNotFoundError:
        print('Unable to generate ID because the inventory has not been created yet.')
        
    else:

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