#importeren van alle modules
  #pygame is nodig, duh
  #os wordt gebruikt bij het inladen van images
  #math wordt om keersommen te kunnen doen
  #sys weet ik ook niet, maar kan nog handig zijn
import pygame, os, math, sys

#is verplicht voor gebruik pygame, vereist wanneer er afgesloten wordt een pygame.quit
pygame.init()

#dit een clock om het aantal frames per second te reguleren
clock = pygame.time.Clock()
clockspeed = 400        #aantal frames per second

#hier wordt de window geinitialiseerd
screenwidth = 1000
screenheight = 600
screen = pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("MARIO")     #dit zet de naam van de window


#Hier worden de sprites ingeladen
dataMap = 'data'        #map waarin de sprites staan
#mario sprite
name = 'mario.bmp'      #naam van het bestand
path = os.path.join(dataMap, name)   #maakt een pad van de map en het bestand
marioSprite = pygame.image.load(path)   #laad het plaateje in
#achtergrond
name = 'achtergrond_groen_blouw.png'    #naam van het bestand
path = os.path.join(dataMap, name)   #maakt een pad van de map en het bestand
background = pygame.image.load(path)   #laad het plaateje in

#animaties

ld = pygame.image.load
ldr = os.path.join
data = 'data'
stil = ld(ldr('data','standing.png'))
walkRight = [ld(ldr(data,'R1.png')), ld(ldr(data,'R2.png')), ld(ldr(data,'R3.png')), ld(ldr(data,'R4.png')), ld(ldr(data,'R5.png')), ld(ldr(data,'R6.png')), ld(ldr(data,'R7.png')), ld(ldr(data,'R8.png')), ld(ldr(data,'R9.png'))]
#walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
walkLeft = [ld(ldr(data,'L1.png')), ld(ldr(data,'L2.png')), ld(ldr(data,'L3.png')), ld(ldr(data,'L4.png')), ld(ldr(data,'L5.png')), ld(ldr(data,'L6.png')), ld(ldr(data,'L7.png')), ld(ldr(data,'L8.png')), ld(ldr(data,'L9.png'))]





#initialisatie van het coordinaten systeem
sx = 0      #scherm x
sy = 0      #scherm y

mariowx = 0     #wereldx van mario
mariowy = 334     #wereldy van mario
mariosx = 0     #de x van mario op het scherm
mariosy = 0     #de y van mario op het scherm

backgroundsx = 0
backgroundsy = 0
backgroundwx = 0
backgroundwy = 0
modifier = 0
backgroundsx2 = background.get_width()
backgroundsy2 = 0
backgroundwx2 = background.get_width()
backgroundwy2 = 0
modifier2 = 1

pressed = True

#snelheden systeem
#alle snelheden enzo zijn in het werled coordinaten systeem
marioxspd = 1.4   #loopsnelheid
marioyspd = 0   #moet nul zijn wordt gebruikt om

mariojmpspd = -15 # de snelheid omhoog die mario krijgt als hij springt
jmpReady = True
gravity = 1


right = False
left = False
WalkCount = 0
def redrawWindow():
    
    global WalkCount
    if WalkCount +1 >= 27:
        WalkCount = 0

    if right:
        screen.blit(walkRight[WalkCount//3], (mariosx, mariosy))
        WalkCount += 1

    elif left:
        screen.blit(walkLeft[WalkCount//3], (mariosx, mariosy))
        WalkCount += 1

    else:
        screen.blit(stil, (mariosx, mariosy))





#Hier begint de main loop, dit is wat er elke frame uitgevoerd wordt
while True:
    #deze klok reguleert de snelheid waarmee de loop uitgevoert wordt
    #als de computer sneller klaar is dan de clockspeed dan wacht hij even voordat hij de volgende frame laad
    clock.tick(clockspeed)
    
    #code om het script te stoppen
    for event in pygame.event.get():        #haalt alle events op. een van de events is het drukken op kruisje
        if event.type == pygame.QUIT:       #als op het kruisje is gedrukt
            pygame.quit()                   #dan sluit pygame af 
        
    #code om link en rechts te lopen
    keys = pygame.key.get_pressed()     #input
    #beweegt naar links
    if keys[pygame.K_a]:
        mariowx -= marioxspd
        left = True
        right = False
    #beweegt naar rechts
    elif keys[pygame.K_d]:
        mariowx += marioxspd
        right = True
        left = False

    else:
        right = False
        left = False
        
    #code om scherm te bewegen
    if mariosx > 800:
        sx += marioxspd
    if mariosx < 100:
        sx -= marioxspd



















        
    #background script van achtergrondje.py
    backgroundsx = backgroundwx - sx
    backgroundsy = backgroundwy - sy
    backgroundsx2 = backgroundwx2 - sx
    backgroundsy2 = backgroundwy2 - sy
    
   
    
    if backgroundsx < background.get_width() * -1:
        modifier += 2
        backgroundwx = background.get_width() * modifier
        
    if backgroundsx2 < background.get_width() * -1:
        modifier2 += 2
        backgroundwx2 = background.get_width() * modifier2
        
    if backgroundsx > background.get_width() * 1:
        modifier -= 2
        backgroundwx = background.get_width() * modifier
        
    if backgroundsx2 > background.get_width() * 1:
        modifier2 -= 2
        backgroundwx2 = background.get_width() * modifier2
    
    #draw fase
    screen.fill((255,255,255)) #clean the screen
    screen.blit(background, (backgroundsx, backgroundsy))
    
    screen.blit(background, (backgroundsx2, backgroundsy2))
    
    #positie van mario op het scherm bepalen
    mariosx = mariowx - sx
    mariosy = mariowy - sy

    redrawWindow()


    pygame.display.update()
    
