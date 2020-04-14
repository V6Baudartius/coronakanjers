print(__name__)

#standard exit code to prevent use as a program
if __name__ == '__main__':
    errormessage = 'This is a module and should not be run alone'
    print(errormessage)
    #quits if run as script
    from sys import exit
    exit(errormessage)

#------------------------------------------------


from . import game as game
from . import menu as menu

def execute():
    game.start()
    counter = 0
    while True:
        counter += 1
        print(counter)
        game.loop()
        
        
        
        if counter>10:
            break
    game.end()   
    menu.start()
    counter = 0
    while True:
        counter += 1
        print(counter)
        menu.loop()
        if counter>10:
            break
    menu.end()
