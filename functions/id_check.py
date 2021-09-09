import csv

def check(file='inventory', action=''):

    while True:
        line = 0
        check = False
        i = input(f'Product ID to {action} [0 to exit]: ')
        if i != '0':
            with open (f'./{file}.csv') as file:
                reader = csv.reader(file)
                lines = list(reader)

            for row in lines:
                if row[0] == str(i):
                    check = True
                    break
                else:
                    line+=1

            if not check:
                print('ID NOT FOUND!')

            elif check:
                break
        else:
            line=0
            break

    return line

    
