print(__name__)
from sys import exit

#standard exit code to prevent use as a program
if __name__ == '__main__':
    errormessage = 'This is a module and should not be run alone'
    print(errormessage)
    #quits if run as script
    exit(errormessage)

#------------------------------------------------

#onze eigen code
from .world import player, enemies, objects, camera, levelcreator
from .UI import klok
from . import settings, globale_variablen as glob, gfx

from time import sleep

#andere shit die geimporteerd moet worden
import pygame

#this wil initialize the game loop
def start(level):
    #pygame
    
    global clock
    clock = pygame.time.Clock() 
    
    #sytze's stopwatch
    global stopwatch
    stopwatch = klok.stopwatch((0,255,0),(255,255,255),820,5,True,True,5,(0,0,0))
    
    #creation
    levelcreator.createlevel(level)
    
    if settings.budgetbeer:
        enemies.achtervolgend_monster(-500,glob.ragnar.y)
    
    #firstdraw
    glob.screen.fill(settings.background_color)
    pygame.display.update()
    
counter = 0
   

#this is what is executed every tick
def loop():

    #predraw -- voor uitleg zie objects.py
        #for object in glob.allObjects:
        #    object.predraw()
        #glob.ragnar.predraw()
    glob.screen.fill(settings.background_color)
    
    #camera
    camera.cameramovement()
    
    #input
    glob.keys = pygame.key.get_pressed()
    
    #----important stuf--------
    for object in glob.allObjects:
        object.update()
    
    #animation
    for object in glob.allObjects:
        object.animation()
    
    #player    
    player.allupdates()    
        
    #draw fase
    for object in glob.allObjects:
        object.postdraw()

    glob.ragnar.postdraw()
    
    for object in glob.voorgrond:
        object.postdraw()
    
    stopwatch.update()
    
    #push the changed surface to screen
    pygame.display.flip()
    
    
    #fps meter
    if settings.printfps:
        global counter
        counter += 1 
        if counter > 120:
            counter = 0
            print(clock.get_fps() )
    

    #exit conditions
        #voor nu alleen venster afsluiten
        #andere events waardoor we uit de loop moeten breken (pauze?) ook hieronder
    for event in pygame.event.get() :        #haalt alle events op. een van de events is het drukken op kruisje
        if event.type == pygame.QUIT:       #als op het kruisje is gedrukt
            pygame.quit()                  #dan sluit pygame af 
            exit()
    
    if glob.keys[pygame.K_ESCAPE]:
        pygame.quit()                  #dan sluit pygame af 
        exit()
        
        
            
    
    #clock -- deze gaat als laatste omdat deze wacht als t script sneller gaat dan gamespeed
    if settings.capfps:
        clock.tick(settings.gamespeed)
    else:
        clock.tick()
    

            
            
            
#dit is opruimcode 
#AKA de allobject lijst moet geleegd en alle refrences naar start variablen moeten verwijderd 
def end():
    
    glob.allObjects.clear()
    glob.allCollisionObjects.clear()
    glob.ragnar = None
    global clock
    clock = None
    global stopwatch
    stopwatch = None
    

    