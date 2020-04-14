print(__name__)

#standard exit code to prevent use as a program
if __name__ == '__main__':
    errormessage = 'This is a module and should not be run alone'
    print(errormessage)
    #quits if run as script
    from sys import exit
    exit(errormessage)

#------------------------------------------------

#onze eigen code
from .world import player, enemies, objects
from .UI import klok
from . import levelcreator

#andere shit die geimporteerd moet worden
import pygame

#this wil initialize the game loop
def start():
    pygame.init()
    #creation
    a = objects.doos(0,0)
    b = objects.grasblok(0,0)
    c = objects.steen(0,0)
    #einde creation




    pass

#this is what is executed every tick
def loop():
    #objects
    for each in glob.allCollisionObjects:
        each.update()
    
    pygame.display.update
    
    
#dit is opruimcode 
#AKA de allobject lijst moet geleegd en alle refrences naar start variablen moeten verwijderd 
def end():
    pass