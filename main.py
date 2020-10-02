import functions

choice = []

for i in range(9):
    choice.append(None)
functions.createhash(choice)

user = input("Choose 'x' or 'o': ")
if user == 'x':
    comp = 'o'
else:
    comp = 'x'

available = [0, 1, 2, 3, 4, 5, 6, 7, 8]

if user == 'x':
    while len(available) >= 1:
        option = int(input('Choose location: '))
        functions.insert(choice, user, option, available)
        functions.createhash(choice)
        if functions.ifwon(choice):
            print('!!!!!!!!!YOU WON!!!!!!!!!!!!!')
            break
        functions.compinsert(choice, available, comp)
        functions.createhash(choice)
        if functions.ifwon(choice):
            print('!!!!!!!YOU LOSE!!!!!!!!!!!!!!')
            break
    else:
        print('!!!!!!MATCH TIED!!!!!!!!!!!')

if user == 'o':
    while len(available) >= 1:
        functions.compinsert(choice, available, comp)
        functions.createhash(choice)
        if functions.ifwon(choice):
            print('!!!!!!!!!YOU LOSE!!!!!!!!!!!!!')
            break
        option = int(input('Choose location: '))
        functions.insert(choice, user, option, available)
        functions.createhash(choice)
        if functions.ifwon(choice):
            print('!!!!!!!!!YOU WON!!!!!!!!!!!!!')
            break
    else:
        print('!!!!!!MATCH TIED!!!!!!!!!!!')
