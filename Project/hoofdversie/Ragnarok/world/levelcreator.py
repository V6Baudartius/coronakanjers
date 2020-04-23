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
boomstronk =            (153,99,67)         #bruin
#----------------------------------------------------
wolk =                  (230,240,240,255)   #blauwwit
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

brickwall_achtergrond = (78,78,78,255)      #grijs alleen dan anders
brick=                  (200,255,255)       #zeer licht grijs



#stone =                 (200,255,255)       #zeer licht grijs
#stonesolid
#darkstone
#darkstonesolid



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

                    elif current == brick:
                        objects.brick(foox, fooy)
                    
                    elif current == boomstronk:
                        objects.boomstronk(foox,fooy)

                    elif current == brickwall_achtergrond:
                        objects.brickwall_achtergrond(foox,fooy)    
                        
#-------------------------------------------------------------------------------                        
                        
    #extra creatie code
    if levelname == 'level_1.png':
        if settings.budgetbeer:
           enemies.tutorialtrigger()   
        objects.text(500,500,(255,255,255), 'dit is level1')
        objects.text(500,550,(255,255,255), 'dit is regel2 van level1')  
        objects.text(500,300,(255,255,255), 'Welkom bij onze Platformer')
        objects.text(500,350,(255,255,255), 'Ik ben Ragnar! Hallo!')
        objects.text(550,400,(255,255,255), 'Je kunt mij laten bewegen met de toetsen A en D')
        objects.text(1550,300,(255,255,255), 'Er is een blokkade! Gelukkig kun je bijlen gooien!')
        objects.text(1575,350,(255,255,255), 'Press F')
        objects.text(500,500,(0,0,0), 'dit is level1')
        objects.text(500,550,(0,0,0), 'dit is regel2 van level1')  
        objects.text(500,200,(0,0,0), 'Welkom bij onze Platformer')
        objects.text(500,250,(0,0,0), 'Ik ben Ragnar! Hallo!')
        objects.text(550,300,(0,0,0), 'Je kunt mij laten bewegen met de toetsen A en D')
        objects.text(650,350, (0,0,0), 'Met CTRL kan je kruipen')
        objects.text(1550,300,(0,0,0), 'Er is een blokkade! Gelukkig kun je bijlen gooien!')
        objects.text(1575,350,(0,0,0), 'Press F')
        objects.text(3000,350,(0,0,0), 'Dit is modder,')
        objects.text(3000,400,(0,0,0), 'daardoor kan je niet zo snel lopen.')
        objects.text(4200,350,(0,0,0), 'Dit is ijs,')
        objects.text(4200,400,(0,0,0), 'daar glijdt je makkelijk op uit!')
        objects.text(5400,350,(0,0,0), 'En kijk uit,')
        objects.text(5400,400,(0,0,0), 'hier vindt je ook nog een sneeuw!')
        objects.text(6500,350,(0,0,0), 'PAS OP,')
        objects.text(6500,400,(0,0,0), 'hier kan je voor het voor eerst dood gaan!')
        objects.text(6500,450,(0,0,0), 'Spring voorzichtig over de spikes heen')
        objects.text(8000,350,(0,0,0), 'Nu wordt het pas echt gevaarlijk,')
        objects.text(8000,400,(0,0,0), 'zie je die enge draak daar achterin het scherm?')
        objects.text(8000,450,(0,0,0), 'Zorg ervoor dat hij je niet op eet!')
        objects.text(10000,100,(0,0,0), 'Oh gelukkig!')
        objects.text(10000,150,(0,0,0), 'Het einde is in zicht!')
        objects.text(10000,200,(0,0,0), 'Ga voor de deur staan en druk op SPACE')
        objects.text(10000,250,(0,0,0), 'om naar het volgende level te gaan!')
        
        
        
        
    elif levelname == 'level_2.png':
        #globale_variablen.ragnar = player.hero(500,500)
        if settings.budgetbeer:
            enemies.achtervolgend_monster(globale_variablen.ragnar.x - 1000, globale_variablen.ragnar.y)                         
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
