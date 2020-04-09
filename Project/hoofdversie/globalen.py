print(__name__)
import pygame

screen = None
dood = None




def scherminitialisatie():
    #changeable variables
    screenwidth = 1000      #wijdte
    screenheight = 600      #hoogte
    caption = 'RAGNAROK'    #naam van het venster
    #end
    print('test')
    scherm = pygame.display.set_mode((screenwidth,screenheight))
    pygame.display.set_caption(caption)
    return scherm

def init():
    global screen
    screen = scherminitialisatie()
    print(test)
    
    global dood
    dood = False
