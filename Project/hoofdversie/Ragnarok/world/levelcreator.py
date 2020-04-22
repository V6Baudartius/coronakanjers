print(__name__)

#standard exit code to prevent use as a program
if __name__ == '__main__':
    errormessage = 'This is a module and should not be run alone'
    print(errormessage)
    #quits if run as script
    from sys import exit
    exit(errormessage)

#--------------COLORCODES----------------------------------
    #rgb waarden: (rood, groen, blauw, alpha)

ragnar =    (255,0,0,255)       #rood
grasblok =  (0,255,0,255)       #groen
doos =      (0,0,255,255)       #blauw
toorts =    (255,255,0,255)     #geel
transition =(255,0,255,255)     #paars
steen =     (0,255,255,255)     #cyaan
grond =     (255,128,0,255)     #bruin
ijs =       (128,255,0,255)     #groenig
spike =     (0,0,0,255)         #negro kleur
bloem1 =    (218,83,2,255)      #oranje
wolk =      (230,240,240,255)   #blauwwit
ijs =       (111,94,236,255)    #ijsblauw

#-----------------------


from .. import globale_variablen, settings, gfx
from . import objects, player

def createlevel(levelname):
    levelimage = gfx.imgload(levelname, 'levels')
    width = levelimage.get_width()
    height = levelimage.get_height()
    
    
    #dit zet automatisch de camera boundaries naar de grote van het level. 
    #tenzij in de settings staat dat dat niet mag
    if not settings.customsize:
        settings.level_w = width*settings.gridsize
        settings.level_h = height*settings.gridsize
    
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
                    
                    foox = x*settings.gridsize
                    fooy = y* settings.gridsize
                    
#--------------------------------------------------------------------------------------- 
 
                    if current == grasblok:
                        objects.grasblok(foox, fooy)
                    
                    elif current == ragnar:
                        globale_variablen.ragnar = player.hero(foox , fooy)
                    
                    elif current == steen:
                        objects.steen(foox, fooy)
                    
                    elif current == doos:
                        objects.doos(foox, fooy)

                    elif current == toorts:
                        objects.kleine_toorts(foox, fooy)
                        
                    elif current == transition:
                        objects.transition(foox, fooy)
                        
                    elif current == grond:
                        objects.grond(foox, fooy)
                        
                    elif current == spike:
                        objects.normalspike(foox, fooy)
                            
                    elif current == bloem1:
                        objects.bloem1(foox, fooy)
                        
                    elif current == wolk:
                        objects.wolk(foox, fooy)
                        
                    elif current == ijs:
                        objects.ijs(foox, fooy)
                    
                        
#-------------------------------------------------------------------------------                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
