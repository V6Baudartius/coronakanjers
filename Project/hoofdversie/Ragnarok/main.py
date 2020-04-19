print(__name__)

#standard exit code to prevent use as a program
if __name__ == '__main__':
    errormessage = 'This is a module and should not be run alone'
    print(errormessage)
    #quits if run as script
    from sys import exit
    exit(errormessage)

#------------------------------------------------




from . import game, menu, globale_variablen, gfx

import pygame

currentlevel = 0
level = ['level_1.png','level_2.png','level_3.png','level_4.png']


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

        currentlevel += 1
        
        gfx.draw(laadscherm)
        pygame.display.update()
        sleep(1)
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    