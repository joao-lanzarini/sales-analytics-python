from inventory_management import *
from inventory_registration import *
from functions import valid_options as v

def menu():

    print('Welcome to Sales Analytics Python')
    print()


    choice = v.valid('[1] Start Purchases.',
                    '[2] Inventory Management.',
                    '[3] View Statistics.')

    if choice == 1: #PURCHASE SYSTEM
        pass

    elif choice == 2: #INVENTORY SYSTEM

        try:
            with open ('inventory.csv', 'r') as file:
                choice2 = v.valid('[1] View inventory.',
                                '[2] Edit items from inventory.')
        except FileNotFoundError:
            choice2 = v.valid('[1] View inventory.',
                            '[2] Edit items from inventory.',
                            "[3] Create your inventory (available only if it's not created yet)")

        if choice2 == 1:
            return 'View Inventory'

        elif choice2 == 2:

            choice3 = v.valid('[1] Add new item to inventory.',
                        '[2] Edit existing items.',
                        '[3] Remove items from inventory.')

            if choice3 == 1:
                return 'Add Items'

            elif choice3 == 2:
                return 'Edit Inventory'

            elif choice3 == 3:
                return 'Remove Items'


        elif choice2 == 3:
            return 'Create Inventory'
        

    elif choice == 3: #VIEW STATISTICS
        pass

    else:
        print('Enter a valid number. (1, 2 or 3)')
        


