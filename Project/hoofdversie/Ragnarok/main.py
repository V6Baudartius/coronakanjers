print(__name__)

#standard exit code to prevent use as a program
if __name__ == '__main__':
    errormessage = 'This is a module and should not be run alone'
    print(errormessage)
    #quits if run as script
    from sys import exit
    exit(errormessage)

#------------------------------------------------



from time import sleep
from . import game, menu, globale_variablen, gfx, settings
from .world.objects import screentext

import pygame

currentlevel = 0
level = ['level_1.png', 'level_2.png','level_3.png','level_4.png']


def execute():
    
    #loading screen script
    laadscherm = gfx.imgload('laadscherm.png')
    gfx.draw(laadscherm)
    pygame.display.update()
    
    
    #artificial delay zodat we naar het laadscherm kunnen kijken
    from time import sleep
    sleep(1)
    
    pygame.init()
    
    while True:    
        #start of game
        global currentlevel
        
        game.start(level[currentlevel])
        globale_variablen.running = True
        while globale_variablen.running:
            game.loop()
        game.end()
        
        if globale_variablen.restart == False:
            nextlevel()
            
            

        

def nextlevel():
    global currentlevel
    #technische shit
    currentlevel += 1
    
    #estethische dingen
    globale_variablen.screen.fill((0,0,0))
    
    if currentlevel == 1:
        screentext(500,450, (255,255,255), 'de story van level 2 is dat ragnar honger had.')
        screentext(500,500, (255,255,255), 'Heel erge honger...')
    elif currentlevel == 2:
        pass
    
    
    
    
    for tekst in globale_variablen.teksten:
        tekst.draw()
    
    pygame.display.flip()
    sleep(2)
    globale_variablen.teksten.clear()
    
    
    
    
    
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
