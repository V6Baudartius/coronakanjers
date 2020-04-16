print(__name__)

#standard exit code to prevent use as a program
if __name__ == '__main__':
    errormessage = 'This is a module and should not be run alone'
    print(errormessage)
    #quits if run as script
    from sys import exit
    exit(errormessage)

#------------------------------------------------

from . import globale_variablen, settings, gfx
from .world import objects, player

def createlevel(levelname):
    levelimage = gfx.imgload(levelname, 'levels')
    width = levelimage.get_width()
    height = levelimage.get_height()
    
    #dit is een black box:
    #ik weet niet hoe het werkt, maar het output een 2d array van grote width*height
    matrix = [[0 for x in range(width)] for x in range(height)]
    
    #nu laden we de kleuren van de pixels van het plaatje in het 2darray
    for x in range(width):
                for y in range(height):
                    matrix[y][x] = levelimage.get_at((x,y))
    
    #nu loopen we er weer doorheen om de waardes af te lezen
    for x in range(width) :
                for y in range(height) :
                    current = matrix[y][x]
                    
                    #als groen
                    if current == (0,255,0,255):
                        #grasblok
                        objects.grasblok(x* settings.gridsize, y* settings.gridsize)
                    #als rood
                    elif current == (255,0,0, 255):
                        #ragnar
                        global ragnar
                        globale_variablen.ragnar = player.hero(x* settings.gridsize, y* settings.gridsize)
                    #als wit
                    elif current == (255, 255, 255, 255):
                        #steen
                        objects.steen(x* settings.gridsize, y* settings.gridsize)
                    #als blauw
                    elif current ==(0, 0, 255, 255):
                        #doos
                        objects.doos(x* settings.gridsize, y* settings.gridsize)
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        