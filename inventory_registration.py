import pandas as pd
import time
from functions import inventory_check as ic
from functions import id_generator as ig
from functions import clear_screen as screen

def createInventory(): # FIRST GENERATION OF THE INVENTORY
    check = ic.checkInventory()

    if not check:

        screen.clear()
        print('Creating your inventory...')
        time.sleep(1)

        with open (f'inventory.csv', 'w') as file:

            file.write('ID, PRODUCT, PRICE, AMOUNT\n')
            print('Your inventory has been created successfully!')

            while True:
                print()
                prod = input('Insert the product name [0 to exit]: ')
                if prod == '0':
                    break

                while True: 
                    price = input(f'Insert the {prod} price ($) [0 to exit]: ').replace(',','.')
                    try:
                        float(price)
                    except ValueError:
                        print()
                        print(f'Error: {price} is not a valid number.')
                        print("Make sure you're not separating thousands.")
                        print()
                    except Exception as error:
                        print(f'ERROR {error}: Something went wrong.')
                    else:
                        break

                if price == '0':
                    break

                while True:
                    amount = input(f'Insert the amount of {prod} available [-1 to exit]: ')
                    try:
                        int(amount)
                    except ValueError:
                        print()
                        print(f'Error: {amount} is not a valid number.')
                        print("Only integer number supported.")
                        print()
                    except Exception as error:
                        print(f'ERROR {error}: Something went wrong.')
                    else:
                        break

                if amount == '-1':
                    break

                screen.clear()

                file.write(f'{ig.generate_id()},{prod.capitalize()},{price},{amount}\n')

        print()
        print('Inventory initialized successfully!')
        print()

    elif check:
        print("Inventory already created.")
        print()


createInventory()
