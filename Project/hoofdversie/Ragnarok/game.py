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

from random import randint
from time import sleep

#andere shit die geimporteerd moet worden
import pygame

glob.background = gfx.imgload('background.png', 'data', False)

#this wil initialize the game loop
def start(level):

    #death shit
    global deathcounter
    deathcounter = 0
    glob.restart = False
    
    #pygame
    global clock
    clock = pygame.time.Clock() 
    
    
    
    #creation
    levelcreator.createlevel(level)
    

        

    
    #firstdraw

    
    #fpscounter
    global counter
    counter = 0
    

   

#this is what is executed every tick
def loop():

    #predraw -- voor uitleg zie objects.py
        #for object in glob.allObjects:
        #    object.predraw()
        #glob.ragnar.predraw()
    
    
    #camera
    camera.cameramovement()
    
    #input
    glob.keys = pygame.key.get_pressed()
    
    #----important stuf--------
    if clock.get_fps() > 50:
        if randint(0,1):
            switch = randint(1,4)
            if switch == 1:
                objects.confetti1(glob.camera_x+randint(0,settings.scherm_wijdte), glob.camera_y)
            if switch == 2:
                objects.confetti2(glob.camera_x+randint(0,settings.scherm_wijdte), glob.camera_y)
            if switch == 3:
                objects.confetti3(glob.camera_x+randint(0,settings.scherm_wijdte), glob.camera_y)
            if switch == 4:
                pass
   
        
    
    
    
    
    
    
    
    
    
    
    
    
    for object in glob.allObjects:
        object.update()
    
    #animation
    for object in glob.allObjects:
        object.animation()
    
    
        
    #player    
    player.allupdates()    
        
    #draw fase
        #draw volgorde is nu:
        #scherm leegmaken
        #objecten
        #tekst
        #ragnar
        #voorgrond
        #stopwatch
    gfx.draw(glob.background, glob.camera_x,glob.camera_y)   
    
    for object in glob.allObjects:
        object.postdraw()
    
    for tekst in glob.teksten:
        tekst.draw()
        
    glob.ragnar.postdraw()
    
    for object in glob.voorgrond:
        object.postdraw()
    
    glob.stopwatch.update()
    
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
        
    if not glob.levend:
        global deathcounter
        deathcounter +=1
        if deathcounter > settings.deathtimer:
            print('restart')
            glob.restart = True
            glob.running = False
            glob.levend = True
    
            
    
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
    glob.voorgrond.clear()
    glob.teksten.clear()
    
    glob.ragnar = None
    global clock
    clock = None    

    