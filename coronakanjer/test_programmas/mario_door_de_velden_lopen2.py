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
clockspeed = 30         #aantal frames per second

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

#initialisatie van het coordinaten systeem
sx = 0      #scherm x
sy = 0      #scherm y

mariowx = 0     #wereldx van mario
mariowy = 330     #wereldy van mario
mariosx = 0     #de x van mario op het scherm
mariosy = 0     #de y van mario op het scherm

backgroundsx = 0
backgroundsy = 0
backgroundwx = 0
backgroundwy = 0
modifier = 1
backgroundsx2 = 0
backgroundsy2 = 0
backgroundwx2 = background.get_width()
backgroundwy2 = 0
modifier2 = 2

pressed = True

#snelheden systeem
#alle snelheden enzo zijn in het werled coordinaten systeem
marioxspd = 15   #loopsnelheid
marioyspd = 0   #moet nul zijn wordt gebruikt om

mariojmpspd = -15 # de snelheid omhoog die mario krijgt als hij springt
jmpReady = True
gravity = 1







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
    #beweegt naar rechts
    if keys[pygame.K_d]:
        mariowx += marioxspd

    sx += 4

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
    screen.blit(marioSprite, (mariosx, mariosy)) #mairo op het scherm tekenen

    
    
    pygame.display.update()
    
