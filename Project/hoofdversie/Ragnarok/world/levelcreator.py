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


ragnar =                (255,0,0,255)       #rood
grasblok =              (0,255,0,255)       #limegroen
doos =                  (0,0,255,255)       #blauw
toorts =                (255,255,0,255)     #geel
transition =            (255,0,255,255)     #roze
#---------------------------------------------------
steen =                 (0,255,255,255)     #cyaan
grond =                 (255,128,0,255)     #oranje
grondsolid =            (150,70,70,255)     #bruin
spike =                 (0,0,0,255)         #zwart
gras =                  (0,100,0,255)       #donkergroen
#----------------------------------------------------
wolk =                  (230,240,240,255)   #zeerlichtgrijs
solidwolk =             (112,139,182,255)   #grijsblauw
ijs =                   (111,94,236,255)    #ijsblauw
ijsblokonder =          (33,77,76,255)      #kotskleur
ijsblokondersolid =     (255,186,221,255)   #huidskleur
ijsblokonder2 =         (163,77,253,255)    #dof paars
#----------------------------------------------------
ijsblokonder2solid =    (188,2,218,255)     #paars
modderblok =            (2,218,136,255)     #groenblauw
sneeuwblokonder =       (79,23,87,255)      #donkerpaars
sneeuwblokondersolid =  (63,12,12,255)      #donkerbruin
sneeuwblok =            (166,253,77,255)    #lichtgroen
#-------------------------------------------------------
brickwall =             (75,75,75,255)      #grijs
brickwallsolid =        (112,112,112,255)   #lichtgrijs
stone =                 (200,255,255)       #zeer licht blauw
stonesolid =            (179,200,103,255)   #mosgroen / kotsgroen
darkstone =             (163,0,0,255)       #donkerrood








#-----------------------


from .. import globale_variablen, settings, gfx
from . import objects, player, enemies
from random import randint

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
                        print('ragnar')
                        globale_variablen.ragnar = player.hero(foox , fooy)
                    
                    elif current == steen:
                        objects.steen(foox, fooy)
                    
                    elif current == doos:
                        objects.doos(foox, fooy)

                    elif current == toorts:
                        objects.kleine_toorts(foox, fooy)
                        
                    elif current == transition:
                        objects.transition(foox, fooy)
                        
                    elif current == grondsolid:
                        objects.grondsolid(foox, fooy)
                        
                    elif current == grond:
                        objects.grond(foox, fooy)
                    
                    elif current == spike:
                        objects.normalspike(foox, fooy)
                        
                    elif current == ijsblokonder:
                        objects.ijsblokonder(foox, fooy)

                    elif current == ijsblokondersolid:
                        objects.ijsblokondersolid(foox, fooy)

                    elif current == ijsblokonder2:
                        objects.ijsblokonder2(foox, fooy)

                    elif current == ijsblokonder2solid:
                        objects.ijsblokonder2solid(foox, fooy)
                            
                    elif current == gras:
                        random = randint(0,6)
                        if random == 0:
                            objects.bloem1(foox, fooy)
                        elif random == 1:
                            objects.bloem2(foox, fooy)
                        elif random == 2:
                            objects.bloem3(foox, fooy)
                        elif random == 3:
                            objects.bloem4(foox, fooy)
                        elif random == 4:
                            objects.gras1(foox, fooy)
                        elif random == 5:
                            objects.gras2(foox, fooy)
                        elif random == 6:
                            objects.gras3(foox, fooy)
                            
                        
                    elif current == wolk:
                        objects.wolk(foox, fooy)
                        
                    elif current == ijs:
                        objects.ijs(foox, fooy)

                    elif current == sneeuwblok:
                        objects.sneeuwblok(foox, fooy)

                    elif current == sneeuwblokonder:
                        objects.sneeuwblokonder(foox, fooy)

                    elif current == sneeuwblokondersolid:
                        objects.sneeuwblokondersolid(foox, fooy)

                    elif current == modderblok:
                        objects.modderblok(foox, fooy)

                    elif current == brickwall:
                        objects.brickwall(foox, fooy)

                    elif current == brickwallsolid:
                        objects.brickwallsolid(foox, fooy)

                    elif current == stone:
                        objects.stone(foox, fooy)

                    elif current == stonesolid:
                        objects.stonesolid(foox, fooy)

                    elif current == darkstone:
                        objects.darkstone(foox, fooy)

                    elif current == solidwolk:
                        objects.solidwolk(foox,fooy)
                        
#-------------------------------------------------------------------------------                        
                        
    #extra creatie code

    if levelname == 'level_1.png':  
        globale_variablen.background = gfx.imgload('background2.png','data',False)
        objects.text(2500,1100,(0,0,0), 'Waar ben ik?')
        objects.text(3081,776,(0,0,0), 'Het laatste wat ik me herinner is Engeland')  
        objects.text(4141,1000,(0,0,0), 'Ik en Olaf waren afgescheiden van de rest,')

        objects.text(5711,1104,(0,0,0), 'maar meer herinner ik me niet')
        objects.text(6946,804,(0,0,0), 'Waar ben ik eigenlijk?')
        objects.text(6946,854,(0,0,0), 'Het is zo droevig hier')
        objects.text(7500,800,(0,0,0), 'laat ik het opvrolijken met een kruipanimatie!')
        objects.text(7500,850,(0,0,0), 'Press CTRL')
        objects.text(8929,292,(0,0,0), 'En ik kan ook bijlen gooien')       
        objects.text(8929,342,(0,0,0), 'Press F')
        objects.text(10667,347,(0,0,0), 'die worp was minstens even goed')
        objects.text(10667,397,(0,0,0), 'als de worpen van Erak')
        objects.text(11609,632,(0,0,0), 'maar toch kreeg hij alle aandacht')
        objects.text(12766,476,(0,0,0), 'Wat een arrogante kwal is hij toch!')
        objects.text(13721,366,(0,0,0), 'Wat is dit voor een gebouw?')
        objects.text(13721,416,(0,0,0), 'Press Space om de deur te openen')
        
    elif levelname == 'level_2.png':
        #globale_variablen.ragnar = player.hero(500,500)
        if settings.budgetbeer:
            enemies.achtervolgend_monster(globale_variablen.ragnar.x - 1000, globale_variablen.ragnar.y, 5) 
    elif levelname == 'level_3.png':           
        enemies.achtervolgend_monster(globale_variablen.ragnar.x - 1000, globale_variablen.ragnar.y, 4)
    elif levelname == 'level_4.png':
        globale_variablen.background = gfx.imgload('background3.png','data',False)
        enemies.achtervolgend_monster(globale_variablen.ragnar.x - 1000, globale_variablen.ragnar.y, 4)
    elif levelname == 'level_5.png':
        globale_variablen.background = gfx.imgload('background3.png','data',False)
        
        
        
        
                            
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
