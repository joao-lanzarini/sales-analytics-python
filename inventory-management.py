import pandas as pd
from random import randint
import csv

inventory = lambda: pd.read_csv('inventory.csv', dtype={'id':str, 'product':str, 'price':float})

def viewInv():
    print(inventory())

def addItems(n=0):    
    inventory()
    if n == 0:
        while True:

            while True:
                rand = randint(1000, 9999)
                if rand not in inventory['id']:

                    id = rand                    
                    break
            
            product = input('Product name (0 to exit): ')

            if product == '0': #CONDIÇÃO DE PARADA
                break

            else:
                price = float(input('Price ($):'))

                with open ('inventory.csv', 'a') as file:
                    file.writelines(f'{id}, {product}, {price:.2f}\n')
            print(f'{product} added at the ID {id}')
            

    else:
        for i in range(n):
            while True:
                rand = randint(1, 9999)
                if rand not in inventory['id']:
                    id = rand
                    break
            product = input('Product name: ')
            price = float(input('Price ($):'))
            with open ('inventory.csv', 'a') as file:
                file.writelines(f'{id}, {product}, {price:.2f}\n')
            print(f'{product} added at the ID {id}')


def editInventory():
    pass

def removeItems():
    pass


viewInv()
