print(__name__)

#standard exit code to prevent use as a program
if __name__ == '__main__':
    errormessage = 'This is a module and should not be run alone'
    print(errormessage)
    #quits if run as script
    from sys import exit
    exit(errormessage)

#------------------------------------------------

from . import settings as set, globale_variablen as glob #our modules
import os, pygame                   #public modules
    

def draw(sprite, x=0, y=0, width=set.gridsize, height=set.gridsize):
    #Om te bepalen waar op het scherm een object getekend moet worden
    #nemen we de huidige positie min de positie van de camera
    drawx = x - glob.camera_x
    drawy = y - glob.camera_y
    drawposition = (drawx,drawy)
    
    glob.screen.blit(sprite, drawposition)
    print('draw')
    

    
def drawrect(color, x, y, width=set.gridsize, height=set.gridsize):
    #drawx = x - glob.camera_x
    #drawy = y - glob.camera_y
    pass
    #drawrectangle = pygame.Rect(drawx,drawy,width,height)  
    #glob.camerasurface.fill(set.background_color, drawrectangle)
    
def imgload(bestandsnaam, mapnaam='data2'):   #de standaard map is 'data'
#__file__ is een unieke variable die de map waarin een script staat geeft
    currentpath = os.path.dirname(__file__) #./game_versies/
   
    stap1 = os.path.join(currentpath, mapnaam) #./game_versies/mapnaam/
    stap2 = os.path.join(stap1, bestandsnaam) #./game_versies/mapnaam/bestandsnaam

    image = pygame.image.load(stap2)
    if set.enablecolorkey:
        image.set_colorkey(set.colorkey)
    image = image.convert()

    return image
    
    
        
