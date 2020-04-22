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
from . import settings, globale_variablen

def scherminitialisatie(height,width,caption):
    
    pygame.init()#argumenten
      
    if settings.fullscreen:
        monitor = pygame.display.Info()
        width = monitor.current_w
        height = monitor.current_h
        
        #dit is voor de camera -- verder niet op letten
        settings.scherm_wijdte = width
        settings.scherm_hoogte = height
        
        scherm = pygame.display.set_mode((width,height), pygame.FULLSCREEN)
    else:
        scherm = pygame.display.set_mode((width,height))
    
    pygame.display.set_caption(caption)
    return scherm
    
def sign(number):
    if number == 0:
        return 0    
    elif number > 0:
        return 1
    else:
        return -1
        
        
def destroyObject(object):
    try:
        globale_variablen.allObjects.remove(object)
        globale_variablen.allCollisionObjects.remove(object)
        globale_variablen.voorgrond.remove(object)
    except:
        pass
   