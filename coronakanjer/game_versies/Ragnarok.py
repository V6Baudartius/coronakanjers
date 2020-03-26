#importeren van alle modules
  #pygame is nodig, duh
  #os wordt gebruikt bij het inladen van images
  #math wordt om keersommen te kunnen doen
  #sys weet ik ook niet, maar kan nog handig zijn 
import pygame, os, math, sys
#test van jochem




#is verplicht voor gebruik pygame, vereist wanneer er afgesloten wordt een pygame.quit
pygame.init()

#dit een clock om het aantal frames per second te reguleren
#note, het aantal frames kan wel minder dan dit worden
clock = pygame.time.Clock()
gamespeed = 60        #aantal frames per second

#hier wordt de window geinitialiseerd
screenwidth = 1000
screenheight = 600
screen = pygame.display.set_mode((screenwidth,screenheight))
#screen is een canvas waarop getekend wordt. alle plaatjes zijn canvassen waarop getekend wordt.
#wat zichtbaar is zal niet veranderen tenzij er display update gedaan wordt waarbij het canvas opnieuw op het scherm getoond wordt

pygame.display.set_caption("RAGNAROK")     #dit zet de naam van de window

sx = 0
sy = 0
#dit zijn de postities van van de 'camera'in onze virtuele wereld.
#alle objecten hebben een wereld positie en uit de positie van het scherm in de wereld 
#en de positie van het object in de wereld berekenen we waar op het scherm iets getekend moet worden.

def getscreenx(wereldx):
    global sx
    drawx = wereldx - sx
    return drawx

def getscreeny(wereldy):
    global sy
    drawy = wereldy - sy
    return drawy

def draw(sprite, wx, wy):
    drawx = getscreenx(wx)
    drawy = getscreeny(wy)
    screen.blit(sprite, (drawx, drawy) )

#dit is de functie om plaatjes in te laden. bestandsextenties moeten aan de naam toegevoegd worden
	#het kan nog niet dealen met plaatjes met witte achtergrond hiervoor is een colorkey nodig
def imgload(filenaam):
	datanaam = 'data'		#de naam van de map waarin de images staan. Zolang de map en het script zichin dezelfde map bevinden en deze naam klopt werkt het script
	
	mappad = os.path.dirname(__file__)		#dit vind het pad van de map waarin het script staat
	datapad = os.path.join(mappad, datanaam)
	filepad = os.path.join(datapad, filenaam)
	image = pygame.image.load(filepad)
	return image

def return1(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0
    

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

        if keys[pygame.K_w]:
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




        #als tweede doen we horizontale movement
        self.wx += self.xspd
        self.hitbox.x = self.wx
        

        muur = False
        for each in self.collisionRange:
            if self.hitbox.colliderect(each.hitbox):
                muur = each
        
        if muur:
            print('collision')
            print(muur)
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
            print('collision')
            print(grond)
            
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
        
 
     
    



#alle objecten die gecreerd worden
#waarschuwing creer nooit twee objecten met collision op dezelfde coordinaten dit verpest het collision script
ragnar = hero(400,300)

grasblokken = list()
grasblokken.append( grasblok(0,500) ) #creert een grasblok en voegt het aan de lijst grassblokken toe op plek 0
grasblokken.append( grasblok(500,500) )
grasblokken.append( grasblok(5000,500) )
grasblokken.append( grasblok(5500,500) )


stenen = list()
stenen.append( steen(0,400) )
stenen.append( steen(800,400) )
stenen.append( steen(650,400) )
stenen.append( steen(210,400) )

dozen = list()
dozen.append( doos( 2000, 500) )
dozen.append( doos( 1500, 200) )
dozen.append( doos( 2800, 400) )
dozen.append( doos( 3500, 400) )
dozen.append( doos( 3800, 100) )
dozen.append( doos( 4500, 500) )

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
    #sx is de linker bovenhoek van de camera en rangar.wx is de absolute positie van ragnar
    sx = ragnar.wx - 200
    sy = ragnar.wy - 200
    
    #draw fase
    screen.fill((0,255,255))
    for each in allCollisionObjects:
        each.update()
        
    ragnar.drawupdate()
    
    pygame.display.update()
    
