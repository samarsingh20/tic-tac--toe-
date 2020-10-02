import random


def insert(ls, usr, pos, avl):
    '''Inserts an item in tictactoe list.'''
    pos -= 1
    ind = avl.index(pos)
    del avl[ind]
    ls[pos] = usr



def compinsert(ls, avl, com):
    try:
        loc = random.choice(avl)
        ls[loc] = com
        del avl[avl.index(loc)]
    except:
        print('Sequence is empty')


def ifwon(ls):
    '''Checks if someone won.'''
    if ls[0] == ls[3] == ls[6] and ls[6] != None:
        return True
    elif ls[1] == ls[4] == ls[7] and ls[7] != None:
        return True
    elif ls[2] == ls[5] == ls[8] and ls[8] != None:
        return True
    elif ls[0] == ls[4] == ls[8] and ls[8] != None:
        return True
    elif ls[2] == ls[4] == ls[6] and ls[6] != None:
        return True
    elif ls[0] == ls[1] == ls[2] and ls[2] != None:
        return True
    elif ls[3] == ls[4] == ls[5] and ls[5] != None:
        return True
    elif ls[6] == ls[7] == ls[8] and ls[8] != None:
        return True
    else:
        return False


def createhash(ls):
    hash = '''\
     |   |
    {}|  {}| {}
     |   |
_______________
     |   |
    {}|  {}| {}
     |   |
_______________
     |   |
    {}|  {}| {}
     |   |'''

    if ls[0] == None:
        p0 = ' '
    else:
        p0 = ls[0]

    if ls[1] == None:
        p1 = ' '
    else:
        p1 = ls[1]

    if ls[2] == None:
        p2 = ' '
    else:
        p2 = ls[2]

    if ls[3] == None:
        p3 = ' '
    else:
        p3 = ls[3]

    if ls[4] == None:
        p4 = ' '
    else:
        p4 = ls[4]

    if ls[5] == None:
        p5 = ' '
    else:
        p5 = ls[5]

    if ls[6] == None:
        p6 = ' '
    else:
        p6 = ls[6]

    if ls[7] == None:
        p7 = ' '
    else:
        p7 = ls[7]

    if ls[8] == None:
        p8 = ' '
    else:
        p8 = ls[8]

    print(hash.format(p0, p1, p2, p3, p4, p5, p6, p7, p8))
    print('\n\n\n\n')
