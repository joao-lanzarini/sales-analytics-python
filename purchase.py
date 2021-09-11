from datetime import datetime
from  functions import buy_id_gen as gen
from  functions import id_check as id
import pandas as pd
import csv

class Purchase():

    def __init__(self):
        self.id = gen.generate_id()
        self.date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.cart = []
        self.price = 0
        self.payMethod = ''

    def addItems(self):

        while True:
        
            check = id.check()

            if check:

                with open ('inventory.csv', 'r') as file:
                    read = csv.reader(file)
                    rows = list(read)
                
                while True: 
                    amount = input("How many? [Press enter if it's just one]: ").strip()
                    if amount != '':
                        try:
                            int(amount)
                        except ValueError:
                            print()
                            print(f'Error: {amount} is not a valid number.')
                            print('The inserted amount must be an integer.')
                            print()
                        except Exception as error:
                            print(f'ERROR {error}: Something went wrong.')
                        else:
                            break

                    else:
                        amount = 1
                        break

                self.cart.append([rows[check][0:3], amount])
                self.price += float(rows[check][2])*int(amount)

            elif not check:
                break

    def payment(self):

        methods = ['Credit Card', 'Debit Card', 'Cash']
        print('[1] Credit Card')
        print('[2] Debit Card')
        print('[3] Cash')

        while True:
            pay = input('Payment Method:  ')

            if pay not in ['1', '2', '3']:
                print()
                print('Please insert a valid number (1, 2 or 3)')

            else:
                break

        self.payMethod = methods[pay-1]



            

        



