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
from . import settings

def scherminitialisatie(height,width,caption):
    #argumenten
    screenwidth = settings.hoogte      #wijdte
    screenheight = settings.wijdte     #hoogte
      
    if settings.fullscreen:
        scherm = pygame.display.set_mode((screenwidth,screenheight), pygame.FULLSCREEN)
    else:
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