import datetime

class Purchase():

    def __init__(self, id, date):
        self.id = id
        self.date = date
        self.cart = []
        self.price = 0

    def addItems(self):
        
        while True:
           item = input("Código do produto: ")



