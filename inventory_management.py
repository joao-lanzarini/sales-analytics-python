import pandas as pd
from random import randint
import csv
from functions import id_check, id_generator


inventory = lambda: pd.read_csv('inventory.csv', dtype={'ID':str, 'PRODUCT':str, 'PRICE':float, 'AMOUNT':int})

def viewInventory(): # VISUALIZE THE INVENTORY
    print(inventory())

def addItems(n=0): # REGISTER PRODUCTS TO THE INVENTORY
    inventory()
    if n == 0:
        while True:

            id = id_generator.generate_id()
            
            product = input('Product name (0 to exit): ').capitalize()

            if product == '0':
                break

            else:
                price = float(input('Price ($):'))

                with open ('inventory.csv', 'a') as file:
                    file.writelines(f'{id}, {product}, {price:.2f}\n')

            print(f'{product} added at the ID {id}')
            

    else:
        for i in range(n): 

            id = id_generator.generate_id()

            product = input('Product name: ').capitalize()
            price = float(input('Price ($):'))

            with open ('inventory.csv', 'a') as file:
                file.writelines(f'{id}, {product}, {price:.2f}\n')

            print(f'{product.capitalize()} added with the ID: {id}')


def editInventory(): # CHANGE PRICE OR AMOUNT

    id = id_check.check(action='edit')

    if id:

        col = int(input('[1] Edit product price\n[2] Edit product amount'))

        with open ('inventory.csv', 'r') as file:
            read = csv.reader(file)
            rows = list(read)

        if col == 1:
            rows[id][2] = input(f'Enter the new {rows[id][1]} price ($): ')

        elif col == 2:
            rows[id][3] = input(f'How many more {rows[id][1]}?')
                
        with open ('inventory.csv', 'w+') as file:
            
            for row in rows:
                file.writelines(f'{row[0]},{row[1]},{row[2]},{row[4]}\n')




def removeItems(): # PERMANENTLY REMOVES A PRODUCT FROM THE INVENTORY

    while True:

        id = id_check.check(action='remove')

        if id:

            with open ('inventory.csv', 'r') as file:
                read = csv.reader(file)
                rows = list(read)

            confirmation = input(f'Are you sure you want to remove {rows[id][1].upper()} registration from the inventory?\n[Y/N]: ').upper().strip()

            while confirmation not in ['Y', 'YES', 'N', 'NO']:
                confirmation = input('Unknown answer.\nType only "Y" or "N": ').upper().strip()

            if confirmation in ['Y', 'YES']:
                rows.pop(id)

                with open ('inventory.csv', 'w+') as file:
            
                    for row in rows:
                        file.writelines(f'{row[0]},{row[1]},{row[2]}\n')

                print()
                print(f'{rows[id][1].capitalize()} permanently deleted!')
                print()

            else:
                continue

        elif not id:
            break


