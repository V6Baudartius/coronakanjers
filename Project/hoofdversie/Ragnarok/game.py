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
from . import settings, levelcreator, globale_variablen as glob

#andere shit die geimporteerd moet worden
import pygame

#this wil initialize the game loop
def start():
    #basics
    pygame.init()
    global clock
    clock = pygame.time.Clock() 
    
    #creation
    levelcreator.createlevel('level_1.png')
    
    #firstdraw
    glob.screen.fill(settings.background_color)
    for each in glob.allCollisionObjects:
        each.update()
    pygame.display.update()
    

   

#this is what is executed every tick
def loop():
    clock.tick(settings.gamespeed)
    #player
    glob.ragnar.gummen()
    keys = pygame.key.get_pressed()
    glob.ragnar.horizontalmovement(keys)
    glob.ragnar.verticalmovement(keys)
    inrange = glob.ragnar.get_inrange()
    glob.ragnar.collision(inrange)
    glob.ragnar.gravity(inrange)
    glob.ragnar.redraw()
    
    
    
    
    pygame.display.update()
    
    #code om het script te stoppen
    for event in pygame.event.get():        #haalt alle events op. een van de events is het drukken op kruisje
        if event.type == pygame.QUIT:       #als op het kruisje is gedrukt
            pygame.quit()                   #dan sluit pygame af 

            
            
            
#dit is opruimcode 
#AKA de allobject lijst moet geleegd en alle refrences naar start variablen moeten verwijderd 
def end():
    pass