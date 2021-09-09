def valid(str1='', str2='', str3=''):

    while True:
        num = 0

        if str1 != '':
            num+=1
            print(str1)
        if str2 != '':
            num+=1
            print(str2)
        if str3 != '':
            num+=1
            print(str3)

        choice = input('Choose -> ').strip()
        print()

        try:
            int(choice)
        except ValueError:
            print('Enter a valid number. (1, 2 or 3)')
            print()
        except Exception as erro:
            print(f'Ops. Error {erro} found.')
            print()
        else:
            if int(choice)>num or int(choice)<1:
                print(f'Enter a valid number. Only from 1 to {num}')
                print()
            else:
                break


    return int(choice)