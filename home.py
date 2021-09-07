from inventory_management import *
from inventory_registration import *

def menu():

    print('Welcome to Sales Analytics Python')
    print()

    while True:

        print('[1] Start Purchases.')
        print('[2] Inventory Management.')
        print('[3] View Statistics.')

        choice = input('Choose -> ')
        try:
            int(choice)
        except ValueError:
            print('Enter a valid number. (1, 2 or 3)')
        except Exception as erro:
            print(f'Ops. Error {erro} found.')
        else:
            break

    if choice == 1: #PURCHASE SYSTEM
        pass

    elif choice == 2: #INVENTORY SYSTEM
        pass

    elif choice == 3: #VIEW STATISTICS
        pass

    else:
        print('Enter a valid number. (1, 2 or 3)')
        


