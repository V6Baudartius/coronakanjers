print(__name__)

#standard exit code to prevent use as a program
if __name__ == '__main__':
    errormessage = 'This is a module and should not be run alone'
    print(errormessage)
    #quits if run as script
    from sys import exit
    exit(errormessage)

#------------------------------------------------


from .UI import klok



#this wil initialize the menu loop
def start():
    pass

#this is what is executed every tick
def loop():
    pass

#dit leegt alle variablen
def end():
    pass