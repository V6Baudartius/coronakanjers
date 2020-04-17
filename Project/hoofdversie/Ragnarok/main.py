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

def execute():
    #loading screen script
    laadscherm = gfx.imgload('laadscherm.png')
    gfx.draw(laadscherm)
    pygame.display.update()
    
    #artificial delay zodat we naar het laadscherm kunnen kijken
    from time import sleep
    sleep(1)
    
    
    
    #start of game
    game.start()
    globale_variablen.running = True
    while globale_variablen.running:
        game.loop()
    game.end()
    

    
