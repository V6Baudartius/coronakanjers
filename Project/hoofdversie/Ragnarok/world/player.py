print(__name__)

#standard exit code to prevent use as a program
if __name__ == '__main__':
    errormessage = 'This is a module and should not be run alone'
    print(errormessage)
    #quits if run as script
    from sys import exit
    exit(errormessage)

#------------------------------------------------

from .. import settings, globale_variablen, gfx
import pygame


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
