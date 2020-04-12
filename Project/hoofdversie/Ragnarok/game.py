print(__name__)

#standard exit code to prevent use as a program
if __name__ == '__main__':
    errormessage = 'This is a module and should not be run alone'
    print(errormessage)
    #quits if run as script
    from sys import exit
    exit(errormessage)

#------------------------------------------------


from .world import player, enemies, objects


#this wil initialize the game loop
def start():
    pass

#this is what is executed every tick
def loop():
    pass
    
#dit is opruimcode 
#AKA de allobject lijst moet geleegd en alle refrences naar start variablen moeten verwijderd 
def end():
    pass