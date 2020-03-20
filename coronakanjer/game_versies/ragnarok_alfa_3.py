#importeren van alle modules
  #pygame is nodig, duh
  #os wordt gebruikt bij het inladen van images
  #math wordt om keersommen te kunnen doen
  #sys weet ik ook niet, maar kan nog handig zijn
import pygame, os, math, sys

#is verplicht voor gebruik pygame, vereist wanneer er afgesloten wordt een pygame.quit
pygame.init()

#dit een clock om het aantal frames per second te reguleren
#note, het aantal frames kan we lminder dan dit worden
clock = pygame.time.Clock()
gamespeed = 60         #aantal frames per second

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
        
        
        #-1 voor links, 0 voor stil, 1 voor rechts
		
		#movement eigenschappen
        self.jmpspd = 10
        self.mvmtspd = 4            #movementspeed
        global gravity 
        gravity = 1
        self.movdir = 0
        
		#hitbox maken
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        self.rect = pygame.Rect(self.wx, self.wy, self.width, self.height)
    
    
    
    def h_movement(self, keys):
        #voordat deze funcite aangeropen word moet er keyboard get pressed gedaan zijn
        #het argument keys is de naam van het array waar de gepressde keys in zitten
        

        if keys[pygame.K_a]:
            self.xspd = -self.mvmtspd
            self.movdir = -1
        elif keys[pygame.K_d]:
            self.xspd = self.mvmtspd
            self.movdir = 1
        else:
            self.xspd = 0
            self.movdir = 0
            
    def collision(self):    
        #update de hitbox zodat ie is waar wij heen lopen
        newx = self.wx + self.xspd
        newy = self.wy + self.yspd    
        self.rect = pygame.Rect(newx, newy, self.width, self.height)
            
        #nu we bewogen hebben gaan we onzelf weer uit objecten halen als we er ergens inzitten
        #als eerste moeten we het dichtsbijzijnde object vinden. AKA het object waar we inzitten
        dichtbijzijnste = everyCollision[0] #dit is de lijst met alle objecten die collision kunnen hebben
        smallestdifference = abs(dichtbijzijnste.rect.centerx - self.rect.centerx)
        
        for each in everyCollision:
            
            newdifference = abs(each.rect.centerx - self.rect.centerx)  #dit neemt het verschil tussen ragnar en het object
            
            if newdifference < smallestdifference:
                smallestdifference = newdifference
                dichtbijzijnste = each
                
        
        #nu we weten wat het dichtbijzijnste object is 
        #verplaatsen we onszelf naar de zijkant van dat object afhankelijk van onze move direction
        
        if self.movdir == (-1):
            #nu vogelen we uit of we uberhaupt colliden met dit object
            if self.rect.colliderect(dichtbijzijnste.rect):
            #we zijn naar links gelopen we moeten onszelf dus aan de rechterkant van het object plaatsen
                self.wx = dichtbijzijnste.rect.right + 1
            #we verplaatsen ons 1 pixel naast de rechterkant van het object
            print ('collision!')
            
        elif self.movdir == 1:
            if self.rect.colliderect(dichtbijzijnste.rect):
                #nu dus aan de linkerkant van het object want we gaan naar rechts
                self.wx = dichtbijzijnste.rect.left - (self.width + 1)
                print ('collision!' )
                


        
    def update(self):
        #coordinates
        self.wx += self.xspd
        self.wy += self.yspd
        #move hitbox
        
        
        #draw
        draw(self.sprite, self.wx, self.wy)   
        
        #de hitbox weer verplaatsen voor volgende cylus
        self.rect = pygame.Rect(self.wx, self.wy, self.width, self.height)
        
        
    def v_movement(self):
        pass
        
    

		
		
		
#dit creeert een lege list
#later voegen we hier alle objecten waarmee onze hero collision kan hebben aan toe
everyCollision = list()
#dit wordt de parentclass van alle objecten waar hero tegenaan kan botsen
class collision():
    def __init__(self, x, y, width, height, sprite):    
        everyCollision.append(self)     #we voegen het object toe aan de lijst
        
        self.sprite = sprite
        self.wx = x
        self.wy = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)    #deze rectangle wordt gebruikt voor collision, het is de 'hitbox'
        
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
        
 
     
    



#alle objecten die gecreerd worden
#waarschuwing creer nooit twee objecten met collision op dezelfde coordinaten dit verpest het collision script
ragnar = hero(100,400)

grasblokken = list()
#grasblokken.append( grasblok(0,500) ) #creert een grasblok en voegt het aan de lijst grassblokken toe op plek 0
#grasblokken.append( grasblok(500,500) )
#grasblokken.append( grasblok(1000,500) )

stenen = list()
stenen.append( steen(0,400) )
stenen.append( steen(800,400) )
stenen.append( steen(650,400) )
stenen.append( steen(390,400) )

print(everyCollision)

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
    
    ragnar.h_movement(keysarray)
    ragnar.hcollision()
    
    
    
    #draw fase
    screen.fill((0,255,255))
    for each in everyCollision:
        each.update()
        
    ragnar.update()
    
    pygame.display.update()
    
