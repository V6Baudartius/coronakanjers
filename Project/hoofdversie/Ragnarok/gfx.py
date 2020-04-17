print(__name__)

#standard exit code to prevent use as a program
if __name__ == '__main__':
    errormessage = 'This is a module and should not be run alone'
    print(errormessage)
    #quits if run as script
    from sys import exit
    exit(errormessage)

#------------------------------------------------

from . import settings as set, globale_variablen  #our modules
import os, pygame                   #public modules
    

def draw(sprite, x=0, y=0):
    #Om te bepalen waar op het scherm een object getekend moet worden
    #nemen we de huidige positie min de positie van de camera
    drawx = x - globale_variablen.camera_x
    drawy = y - globale_variablen.camera_y
    drawposition = (drawx,drawy)
    globale_variablen.screen.blit(sprite, drawposition)
    
def drawrect(rectangle, color):
    rectangle.x -= globale_variablen.camera_x
    rectangle.y -= globale_variablen.camera_y
    
    pygame.draw.rect(globale.variablen.screen, color, rectangle)
    
    
    
def imgload(bestandsnaam, mapnaam='data'):   #de standaard map is 'data'
#__file__ is een unieke variable die de map waarin een script staat geeft
    currentpath = os.path.dirname(__file__) #./game_versies/
   
    stap1 = os.path.join(currentpath, mapnaam) #./game_versies/mapnaam/
    stap2 = os.path.join(stap1, bestandsnaam) #./game_versies/mapnaam/bestandsnaam

    image = pygame.image.load(stap2)
    return image    
