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

    def addItems(self):
        
        check = False
        i = input('Product ID [0 to exit]: ')
        if i != '0':
            check = id.check(i)
            while not check:
                print('ID NOT FOUND!')
                i = input('Product ID [0 to exit]: ')
                if i == '0':
                    break
                else:
                    check = id.check(i)

        if check:

            with open ('inventory.csv', 'r') as file:
                read = csv.reader(file)
                rows = list(read)

            

        



