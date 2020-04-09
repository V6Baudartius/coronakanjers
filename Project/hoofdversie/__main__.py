#importeren van alle modules
  #pygame is nodig, duh
  #os wordt gebruikt bij het inladen van images
  #math wordt om keersommen te kunnen doen
  #sys weet ik ook niet, maar kan nog handig zijn
  #time wordt gebruikt bij het maken van tijdsgerelateerde scripts
import pygame, os, math, sys, time

import globalen
from enemies import * 
from gfx import *

globalen.init()
print (globalen.screen)

#pygame init initialiseerd automatisch alle pygame functies die 
#geinitialiseerd moeten worden
pygame.init()

#-----------------------

#frameratemanager:

#de pygame klok is een wacht script:
    #als de pc sneller dan de gamespeed frames laad,
    #voert de klok een wait uit.
gamespeed = 60 #aantal frames per second
clock = pygame.time.Clock()
 
#--------------------------------
 




#positie van de 'camera' in de virtuele wereld
camera_x = 0
camera_y = 0

#--------------------


#----------------



#-------------------------------------

#dit wordt gebruikt bij collision
def return1(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0
    
#-------------------------------------

#hierin staan alle functies en variabelen die ons karakter heeft
class hero():
    def __init__(self, x, y):
		#draw variablen
        self.sprite = imgload('Ragnar.png')
        
		
	#coordinaten
        self.wx = x
        self.wy = y
        self.xspd = 0
        self.yspd = 0
        
		
	#movement eigenschappen
        self.jmpspd = 20
        self.mvmtspd = 10            #movementspeed
        global gravity 
        gravity = 1
        self.movdir = 0
        
	#hier maken we een rectangle die we kunnen gebruiken voor collision
        width = self.sprite.get_width()
        height = self.sprite.get_height()
        self.hitbox = pygame.Rect(self.wx, self.wy, width, height)

        #dit is de zoekrange voor objecten om collision mee te doen
        #de collisionrange is de lijst van objecten die zich binnen 200 pixels van de hero bevinden
        #en waar we dus mee kunnen colliden
        self.xrange = 500
        self.yrange = 500
        self.collisionRange = list()


    def movementupdate(self, keys):    

        #begin horizontale input

        #keys[pygame.K_] geeft 0 of 1 als het is ingedrukt of niet
        # als we dus beide waarden bij elkaar optellen met de waarde van a negatief
        #dan krijgen we -1 als we links indrukken, 0 als we beide indrukken en 1 als we recht indrukken
        direction = keys[pygame.K_d] - keys[pygame.K_a]
        
        self.xspd = direction * self.mvmtspd



        #einde horizontale input

        #begin verticale input
        global gravity
        self.yspd += gravity

        if keys[pygame.K_w] and spriteveranderalsdood:
            self.yspd = -self.jmpspd

        #einde verticale input











        #begin collision 
        #hier wordt xspd en yspd definitief
        #veranderingen hieraan moeten dus hiervoor gebeuren
        
        #als eerste bepalen we welke objecten dichtbij zijn.
        #dit doen we om het gebruik van rect.collide te minimaliseren zodat het programma efficienter wordt
        #de range waarin dit gebeurt is net iets groter dan de snelheid zodat alles waar
        #we tegenaan zouden kunnen lopen sowieso in de range valt
        global allCollisionObjects
        self.collisionRange.clear()
        
        for each in allCollisionObjects:
            deltax = abs(each.hitbox.centerx - self.hitbox.centerx) #abs geeft de absolute waarde.
            deltay = abs(each.hitbox.centery - self.hitbox.centery) #dit rekend dus de afstanden tussen de objecten uit
            inrange = deltax < self.xrange and deltay < self.yrange 
            if inrange:
                self.collisionRange.append(each)
            #als inrange dan voeg toe aan de lijst
        #einde collisionrange bepalen



        if spriteveranderalsdood == False:
            self.collisionRange.clear()
            
        #als tweede doen we horizontale movement
        if spriteveranderalsdood:
            self.wx += self.xspd
        self.hitbox.x = self.wx
        

        muur = False
        for each in self.collisionRange:
            if self.hitbox.colliderect(each.hitbox):
                muur = each
        
        if muur:
            #print('collision')
            #print(muur)
            #dus als er een object aan muur toegewezen is
            
            #we verplaatsen ons naar de linker of rechterkant van het object
            #afhankelijk van de bewegingsrichting
            direction = return1(self.xspd)
            #dit geeft -1 als links en 1 als rechts
            if direction == 1:
                self.hitbox.right = muur.hitbox.left
            if direction == -1:
                self.hitbox.left = muur.hitbox.right
            #nu staat de hitbox op de juiste plek en moeten we het karakter even meenemen
            self.wx = self.hitbox.x
            self.xspd = 0
        #einde hmovement

        
        #nu komt de verticale movement
        #deze gaat hetzelfde alleen dan met y, er zijn dus minder comments
        self.wy += self.yspd
        self.hitbox.y = self.wy
        grond = False
        #grond is hier hetzelfde als muur in het vorige stuk
        #omdat we hier verticaal bezig zijn heb ik de naam aangepast
        for each in self.collisionRange:
            if self.hitbox.colliderect(each.hitbox):
                grond = each
        
        if grond:
            #print('collision')
           # print(grond)
            
            direction = return1(self.yspd)
            #1 is naar beneden, -1 is omhoog
            
            if direction == 1:
                self.hitbox.bottom = grond.hitbox.top
            if direction == -1:
                self.hitbox.top = grond.hitbox.bottom
            self.wy = self.hitbox.y
            self.yspd = 0
        #einde vmovement

        #eindecollision




        


        
        
    def drawupdate(self):
        #draw
        draw(self.sprite, self.wx, self.wy)   

        
spriteveranderalsdood = True           

        
		
		
		
#dit creeert een lege list
#later voegen we hier alle objecten waarmee onze hero collision kan hebben aan toe
allCollisionObjects = list()
#dit wordt de parentclass van alle objecten waar hero tegenaan kan botsen
class collision():
    def __init__(self, x, y, width, height, sprite):    
        allCollisionObjects.append(self)     #we voegen het object toe aan de lijst
        
        self.sprite = sprite
        self.wx = x
        self.wy = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(x, y, width, height)    #deze rectangle wordt gebruikt voor collision, het is de 'hitbox'
        
    def update(self):
        draw(self.sprite, self.wx, self.wy)
        

class grasblok(collision):
    def __init__(self, x, y):
    
        sprite = imgload('grasblok.png')
        #de sprite = 500 bij 100
        wijdte = sprite.get_width()
        hoogte = sprite.get_height()
        super().__init__(x, y, wijdte, hoogte, sprite)
        
                
class steen(collision) :   
    def __init__(self, x, y):
    
        sprite = imgload('steen.png')
        #de sprite is 50 bij 100
        wijdte = sprite.get_width()
        hoogte = sprite.get_height()
        super().__init__(x, y, wijdte, hoogte, sprite)

class doos(collision):
    def __init__(self, x, y):
        sprite = imgload('doos.png')
        wijdte = sprite.get_width()
        hoogte = sprite.get_height()
        super().__init__(x, y, wijdte, hoogte, sprite)
        
class enemy_lopend():
    def __init__(self, x, y):
        self.sprite = imgload('enemy.bmp')
        self.x = x
        self.y = y
        width = self.sprite.get_width()
        height = self.sprite.get_height()
        self.hitbox = pygame.Rect(x,y,width,height)
        self.direction = 1
        self.speed = 4
        
    def movementupdate(self):

        self.hitbox.x = self.x                   
        self.hitbox.y = self.y


        if self.direction == 1:
            test_x = self.hitbox.right + self.speed
        elif self.direction == -1:    
            test_x = self.hitbox.left + self.speed*-1
        
        test_pos = (test_x, self.y-50)
        global allCollisionObjects
        print(test_pos)
        for each in allCollisionObjects:
        
            if each.hitbox.collidepoint(test_pos):
                self.direction *= -1
                print('collision')

        self.x += self.speed*self.direction
        
        
        
    def drawupdate(self):
        draw(self.sprite, self.x, self.y)
        
    
    
 



#alle objecten die gecreerd worden
#waarschuwing creer nooit twee objecten met collision op dezelfde coordinaten dit verpest het collision script
#BEGIN LEVELTEST:
#al het andere is oud en van ragnarok gekopieerd

def lvlload(filenaam):
	datanaam = 'levels'		#de naam van de map waarin de images staan. Zolang de map en het script zichin dezelfde map bevinden en deze naam klopt werkt het script
	
	mappad = os.path.dirname(__file__)		#dit vind het pad van de map waarin het script staat
	datapad = os.path.join(mappad, datanaam)
	filepad = os.path.join(datapad, filenaam)
	lvl = pygame.image.load(filepad)
	return lvl


class levelparent():
    def __init__(self):
            source = lvlload('level_3.png')
            width = source.get_width()
            height = source.get_height()
            gridsize = 100
            
            matrix = [[0 for x in range(width)] for x in range(height)]

            #deze code stopt de kleur van alle pixels in een 2d array
            #later lezen we dit array af en creeeren we objecten gebaseerd op de kleurwaarden in het array
            for x in range(width):
                for y in range(height):
                    matrix[y][x] = source.get_at((x,y))
            print(matrix)
            dozen = list()
            grasblokken = list()
            stenen = list()
            


        
            
            for x in range(width) :
                for y in range(height) :
                    current = matrix[y][x]
                    if current == (0,255,0,255):
                        grasblokken.append( grasblok(x*gridsize, y*gridsize))
                    elif current == (255,0,0, 255):
                        global ragnar
                        ragnar = hero(x*gridsize, y*gridsize)
                    elif current == (255, 255, 255, 255) :
                        stenen.append(steen(x*gridsize, y*gridsize))
                    elif current ==(0, 0, 255, 255):
                        dozen.append( doos(x*gridsize, y*gridsize))
#EINDE LEVELTEST                    
#BEGIN STOPWATCH

#Dit slaat de tijd op op het moment dat dit script wordt gestart.
#time.gmtime() geeft een aray aan variabelen(?). Waarbij [3] de uren geeft, [4] de minuten en [5] de seconden.
start = time.gmtime()

#hier begint de customclock class. En dan kan je denken:"Sytze, waarom noem je class niet gwn clock?". NOU OMDAT PYGAME AL EEN OBJECT HEEFT GENAAMD CLOCK!!!!!!!!!!!    
class stopwatch():
    def __init__(self, kleurrect, kleurtijd, xleft, ytop, uren, outline, dikte, kleuroutline, start):
        self.kleurrect = kleurrect
        self.kleurtijd = kleurtijd
        self.xleft = xleft
        self.ytop = ytop
        self.uren = uren
        self.outline = outline
        self.dikte = dikte
        self.kleuroutline = kleuroutline
        self.start = start
#Hier begint de functie drawclock waarin een stopwatch wordt geïnitïeerd en daarna ook getekend/
    def drawstopwatch(self):
        #Door global screen te doen haal kan je screen gebruiken die eerder gedefnieerd is.
        #Dit komt doordat screen zich in de globale sector bevindt en deze class zit in de lokale sector.
        
        #Slaat de tijd op van nu. Dit is dus de steeds veranderende tijd.
        now = time.gmtime()
        #Hier wordt het verschil in seconden berekent tussen de starttijd en de tijd van nu.
        seconde = now[5]-self.start[5]
        #Hier wordt het verschil in minuten berekent tussen de starttijd en de tijd van nu.
        minuut = now[4]-self.start[4]
        #Hier wordt het verschil in uren berekent tussen de starttijd en de tijd van nu.
        uur = now[3]-self.start[3]

        #De lettertype grootte
        grootte = 25

        #De font (lettertype) wordt  hier bepaald.
        default_font = pygame.font.Font("C:/Windows/Fonts/comicz.TTF", grootte)
        #Als het verschil in seconden negatief wordt, wordt het met behulp van dit trucje weer goed positief gemaakt.
        if seconde < 0:
            seconde += 60
            minuut -= 1
            
        #Als het verschil in minuten negatief wordt, wordt het met behulp van dit trucje weer goed positief gemaakt.
        if minuut < 0:
            minuut += 60
            uur -= 1
            
        #Het rechthoekje met tijd erin kan verschillen door het hebben van uren in de tijd of niet. De breedte van het rechthoekje wordt hier dan gecorigeerd.
        if self.uren:
            breedte = 170    
        else:
            breedte = 105
            
        #De hoogte blijft wel altijd gelijk.    
        hoogte = 30    

        #Als self.outline is True dan wordt er eerst een grotere rechthoek getekent waarna het kleinere het rechthoek er overheen wordt getekent waardoor het lijkt
        #alsof er een outline is getekent om het kleinere rechthoek heen.
        if self.outline and self.dikte>0 and self.dikte<10:
            #grotere rechthoek wordt getekent
            pygame.draw.rect(globalen.screen, self.kleuroutline, (self.xleft-5-self.dikte, self.ytop+5-self.dikte, breedte+2*self.dikte, hoogte+2*self.dikte))
        #kleinere rechthoek wordt getekent    
        pygame.draw.rect(globalen.screen, self.kleurrect, (self.xleft-5, self.ytop+5, breedte, hoogte))
        #als self.uren false is dan worden de uren niet in het tijdsblokje gegeven. Anders wel.
        if not self.uren:
            #tekst zonder uren
            tijd_tekst = default_font.render(str(minuut).zfill(2) + ' : ' + str(seconde).zfill(2), True, self.kleurtijd)
        else:
            #tekst met uren
            tijd_tekst = default_font.render(str(uur).zfill(2) + ' : ' + str(minuut).zfill(2) + ' : ' + str(seconde).zfill(2), True, self.kleurtijd)
        #tekst wordt getekent
        globalen.screen.blit(tijd_tekst, (self.xleft,self.ytop))

#EINDE STOPWATCH

creatie = levelparent()
enemy1 = enemy_lopend(2000,400)
michiel = monster(-420, 69, 0.1)
#De stopwatch wordt hier geinitialiseerd
klok1 = stopwatch((0,255,0),(255,255,255),820,5,True,True,5,(0,0,0),start)


print(allCollisionObjects)

#Hier begint de main loop, dit is wat er elke frame uitgevoerd wordt
while True:
    #deze klok reguleert de snelheid waarmee de loop uitgevoert wordt
    #als de computer sneller klaar is dan de clockspeed dan wacht hij even voordat hij de volgende frame laad
    clock.tick(gamespeed)
    
    #code om het script te stoppen
    for event in pygame.event.get():        #haalt alle events op. een van de events is het drukken op kruisje
        if event.type == pygame.QUIT:       #als op het kruisje is gedrukt
            pygame.quit()                   #dan sluit pygame af 
        
    #code om link en rechts te lopen
    keysarray = pygame.key.get_pressed()     #input
    
    
    ragnar.movementupdate(keysarray)
        

    #dit is temporary code om de camera mee te laten bewegen met de hero
    #camera_x is de linker bovenhoek van de camera en rangar.wx is de absolute positie van ragnar
    camera_x = ragnar.wx - 350
    camera_y = ragnar.wy - 200
    
    #draw fase
    globalen.screen.fill((0,255,255))
    for each in allCollisionObjects:
        each.update()
    enemy1.movementupdate
        
    michiel.update()
    #print(michiel.x)
    if michiel.x + 500 > ragnar.wx and spriteveranderalsdood:
        ragnar.sprite = imgload('ragnar_dood.png')
        spriteveranderalsdood = False

    klok1.drawstopwatch()  #de klok wordt hier getekent  
    ragnar.drawupdate()
    enemy1.drawupdate()    
    
    pygame.display.update()
    
