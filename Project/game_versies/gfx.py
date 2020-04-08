import pygame, os, math, sys, time
import globalen


print(__name__)
    
    
def draw(sprite, x, y):
    global camera_x
    global camera_y
    
    camera_x = 0
    camera_y = 0
#Om te bepalen waar op het scherm een object getekend moet worden
#nemen we de huidige positie min de positie van de camera
    drawx = x - camera_x
    drawy = y - camera_y
    
    drawposition = (drawx,drawy)
    
    globalen.screen.blit(sprite, drawposition)

def imgload(bestandsnaam, mapnaam='data'):   #de standaard map is 'data'
#__file__ is een unieke variable die de map waarin een script staat geeft
    currentpath = os.path.dirname(__file__) #./game_versies/
   
    stap1 = os.path.join(currentpath, mapnaam) #./game_versies/mapnaam/
    stap2 = os.path.join(stap1, bestandsnaam) #./game_versies/mapnaam/bestandsnaam

    image = pygame.image.load(stap2)
    return image
    
