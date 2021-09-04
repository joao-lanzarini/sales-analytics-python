import pandas as pd
from random import randint

inventory = pd.read_csv('inventory.csv')

while True:
    rand = randint(1, 9999)
    if rand not in inventory['id']:
        id = rand
        print(id)
    else:
        print(f'ID {id} already in use')
        break

