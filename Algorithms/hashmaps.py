voted = dict()

def checkname(name):
    if voted.get(name):
        print('get out')
    else:
        print('go vote')
        voted[name] = True
checkname('tom')
checkname('tom')



