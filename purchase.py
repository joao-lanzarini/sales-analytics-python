class Purchase():

    def __init__(self, id, date):
        self.id = id
        self.date = date
        self.cart = []
        self.price = 0

    def addItems(self):
        
        while True:
           tem = input("Código do produto: ")




i = ['apple', 'banana', 'meat', 'candies']
c = Purchase('001', 25, i, 30, 'cash')

