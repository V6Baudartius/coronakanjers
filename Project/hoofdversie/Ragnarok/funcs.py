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
from . import settings as set, globale_variablen as glob

def scherminitialisatie():
    
    pygame.init()#argumenten
      
    if set.fullscreen:
        monitor = pygame.display.Info()
        width = monitor.current_w
        height = monitor.current_h
        
        #dit is voor de camera -- verder niet op letten
        set.scherm_wijdte = width
        set.scherm_hoogte = height
        
        scherm = pygame.display.set_mode((width,height), pygame.FULLSCREEN)
    else:
        scherm = pygame.display.set_mode((set.scherm_wijdte, set.scherm_hoogte))
    
    pygame.display.set_caption(set.caption)
    return scherm
    
def updatescreen():
    glob.camerasurface = pygame.transform.scale2x(glob.camerasurface)
    glob.screen.blit(glob.camerasurface,(0,0))
    glob.camerasurface = pygame.transform.scale
    print(glob.screen)
    pygame.display.flip()
    
    
    
    
    
    
    
def sign(number):
    if number == 0:
        return 0    
    elif number > 0:
        return 1
    else:
        return -1
        
        
def destroyObject(object):
    try:
        glob.allObjects.remove(object)
        glob.allCollisionObjects.remove(object)
    except:
        pass
   