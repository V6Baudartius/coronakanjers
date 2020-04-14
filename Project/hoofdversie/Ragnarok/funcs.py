print(__name__)

#standard exit code to prevent use as a program
if __name__ == '__main__':
    errormessage = 'This is a module and should not be run alone'
    print(errormessage)
    #quits if run as script
    from sys import exit
    exit(errormessage)

#------------------------------------------------

import pygame

def scherminitialisatie(height,width,caption):
    #argumenten
    screenwidth = height      #wijdte
    screenheight = width      #hoogte
    caption = caption    #naam van het venster
    
    
    scherm = pygame.display.set_mode((screenwidth,screenheight))
    pygame.display.set_caption(caption)
    return scherm
    
def sign(number):
    if number == 0:
        return 0    
    elif number > 0:
        return 1
    else:
        return -1