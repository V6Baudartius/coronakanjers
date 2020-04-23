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
from .UI import klok

import pygame

currentlevel = -1

level = ['level_1.png','level_2.png','level_3.png','level_4.png']
    




            
            

        

def nextlevel():
    global currentlevel
    #technische shit
    
    
    #estethische dingen
    globale_variablen.screen.fill((0,0,0))
    
    if currentlevel == 0:
        screentext(500,450, (255,255,255), 'Welkom bij SPOLAS een zelfgeprogrammeerde en getekende game')
        screentext(500,500, (255,255,255), 'Je controleert je karakter met: W, A, D, F, spatie en Ctrl')
    
    if currentlevel == 1:
        screentext(500,450, (255,255,255), 'de mysterieuse poort verplaatste me naar een nieuwe locatie')
        screentext(500,500, (255,255,255), 'deze plek was alleen veel vijandiger')
        screentext(500,550, (255,255,255), 'maar ik ga bewijzen dat ik dit aan kan')
        screentext(500,600, (255,255,255), 'deze plek was alleen veel vijandiger')
    elif currentlevel == 2:
        pass
    
    currentlevel += 1
    
def execute():

    #sytze's stopwatch
    globale_variablen.stopwatch = klok.stopwatch((0,255,0),(255,255,255),820,5,True,True,5,(0,0,0))

    
    #loading screen script
    laadscherm = gfx.imgload('laadscherm.png')
    gfx.draw(laadscherm)
    pygame.display.update()
    
    
    
    #artificial delay zodat we naar het laadscherm kunnen kijken
    from time import sleep
    sleep(1)
    
    pygame.init()
    
    while True:    
        nextlevel()
        #start of game
        global currentlevel
        
        game.start(level[currentlevel])
        globale_variablen.running = True
        while globale_variablen.running:
            game.loop()
        game.end()
        
        if globale_variablen.restart == False:
            nextlevel()    
    
    for tekst in globale_variablen.teksten:
        tekst.draw()
    
    pygame.display.flip()
    sleep(2)
    globale_variablen.teksten.clear()
    
    
    
    
    
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
