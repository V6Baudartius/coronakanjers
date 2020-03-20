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
class hero:
    def __init__(self):
		#draw variablen
        self.sprite = imgload('Ragnar.png')
        
		
		#coordinaten
        self.wx = 200
        self.wy = 0
		
		
		#physics eigenschappen
        
		
		
		
		#collision variablen

		
		
		
#dit creeert een lege list
#later voegen we hier alle objecten waarmee onze hero collision kan hebben aan toe
everyCollision = list()
#dit wordt de parentclass van alle objecten waar hero tegenaan kan botsen
class collision:
    def __init__(self,x,y,width,height):    
        everyCollision.append(self)
        #we voegen het object toe aan de lijst
        self.wx = x
        self.wy = y
        self.width = width
        self.heigth = height
        self.rect = pygame.Rect(x, y, width, height)




ragnar = hero()
doos1 = collision(400,300,100,200)
doos2 = collision(800,300,100,100)

for each in everyCollision:
    print(each.wx, each.wy) 




dataMap = 'data'        #map waarin de sprites staan
#mario sprite

#achtergrond
name = 'achtergrond_groen_blouw.png'    #naam van het bestand
path = os.path.join(dataMap, name)   #maakt een pad van de map en het bestand
background = imgload('achtergrond_groen_blouw.png')   #laad het plaateje in

#initialisatie van het coordinaten systeem
sx = 0      #scherm x
sy = 0      #scherm y

mariowx = 0     #wereldx van mario
mariowy = 330     #wereldy van mario
mariosx = 0     #de x van mario op het scherm
mariosy = 0     #de y van mario op het scherm

backgroundwx = 0
backgroundwy = 0
backgroundsx = 0
backgroundsy = 0
pressed = True

#snelheden systeem
#alle snelheden enzo zijn in het werled coordinaten systeem
marioxspd = 5   #loopsnelheid
marioyspd = 0   #moet nul zijn wordt gebruikt om

mariojmpspd = -15 # de snelheid omhoog die mario krijgt als hij springt
jmpReady = True
gravity = 1


yground = 300




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
    keys = pygame.key.get_pressed()     #input
    #beweegt naar links
    if keys[pygame.K_a]:
        mariowx -= marioxspd
    #beweegt naar rechts
    if keys[pygame.K_d]:
        mariowx += marioxspd

    if keys[pygame.K_w]:
        sx += 50
        pressed = True
    else:
        pressed = False
        
    if keys[pygame.K_s]:
        sx -= 50
        pressed = True
    else:
        pressed = False

    
    #draw fase
    screen.fill((255,255,255)) #clean the screen
    
    

    

    backgroundsx = backgroundwx - sx
    backgroundsy = backgroundwy - sy
    screen.blit(background, (backgroundsx, backgroundsy))
    
    #positie van mario op het scherm bepalen
    mariosx = mariowx - sx
    mariosy = mariowy - sy
    screen.blit(ragnar.sprite, (mariosx, mariosy)) #mairo op het scherm tekenen

    
    
    pygame.display.update()
    
