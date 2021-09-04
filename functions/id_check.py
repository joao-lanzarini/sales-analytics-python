import csv

def check(id):

    check = False
    line = 0

    with open ('./inventory.csv') as file:
        reader = csv.reader(file)
        lines = list(reader)

        for row in lines:
            if row[0] == str(id):
                check = True
                break
            else:
                line+=1
            
    if check:
        return line

    elif not check:
        return False

    
