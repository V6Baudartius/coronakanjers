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


level = ['level_1.png','level_2.png','level_3.png','level_4.png','level_5.png']


    




            
            

        

def nextlevel():
    global currentlevel
    #technische shit
    
    currentlevel += 1
    #estethische dingen
    globale_variablen.screen.fill((0,0,0))
    
    if currentlevel == 0:
        screentext(500,450, (255,255,255), 'Welkom bij SPOLAS een zelfgeprogrammeerde en getekende game')
        screentext(500,500, (255,255,255), 'Je controleert je karakter met: W, A, D, F, spatie en Ctrl')
    
    if currentlevel == 1:
        screentext(500,450, (255,255,255), 'De mysterieuse poort verplaatste me naar een nieuwe locatie')
        screentext(500,500, (255,255,255), 'Deze plek was alleen veel vijandiger')
        screentext(500,550, (255,255,255), 'Maar ik ga bewijzen dat ik dit aan kan')
        screentext(500,600, (255,255,255), 'Maar ik ben beter dan mijn broer')
    elif currentlevel == 2:
        screentext(500,450, (255,255,255), 'Deze uitdagingen zijn zeker door odin zelf gemaakt')
        screentext(500,500, (255,255,255), 'Daar ik zal bewijzen dat ik beter ben dan mijn broer Erak')
        
    elif currentlevel == 3:
        screentext(500,450, (255,255,255), 'Ik herinner me nog de tijd dat we jong waren ')
        screentext(500,500, (255,255,255), 'Erak en ik ruzieden altijd ')
        screentext(500,550, (255,255,255), 'Maar eigenlijk hielden we wel van elkaar ')
        
    elif currentlevel == 4:
        screentext(500,450, (255,255,255), 'Ja ik en Erak waren echte broeders ')
        screentext(500,500, (255,255,255), 'en daarom heb ik zoveel spijt')
        screentext(500,550, (255,255,255), 'In Engeland liet ik hem achter in handen van de vijand')
        screentext(500,600, (255,255,255), 'Freya, vergeef me')
        
    elif currentlevel == 5:
        
    
    
    
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
        if globale_variablen.restart == False:

            globale_variablen.teksten.clear()
            nextlevel()
        
            for tekst in globale_variablen.teksten:
                tekst.draw()
    
            pygame.display.flip()
            sleep(4)
            globale_variablen.teksten.clear()
    
        
        #start of game
        global currentlevel
        
        game.start(level[currentlevel])
        globale_variablen.running = True
        while globale_variablen.running:
            game.loop()
        game.end()
        
            
    

    
    
    
    
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
