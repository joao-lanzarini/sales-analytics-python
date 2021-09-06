def checkInventory():   
    try:
        with open ('inventory.csv', 'r') as file:
            return True
    except FileNotFoundError:
        return False
