print(__name__)

#standard exit code to prevent use as a program
if __name__ == '__main__':
    errormessage = 'This is a module and should not be run alone'
    print(errormessage)
    #quits if run as script
    from sys import exit
    exit(errormessage)

#------------------------------------------------

from .. import settings, globale_variablen, gfx, funcs
from . import objects
import pygame

#-----loopfuncties-------
#keys = pygame.key.get_pressed()
#horizontalmovement(keys)
#verticalmovement(keys)
#inrange = get_inrange()
#collision(inrange)
#gravity(inragne)
#-------

#hierin staan alle functies en variabelen die ons karakter heeft
class hero():
    def __init__(self, x, y):
		#draw variablen
        self.grote_ragnar = gfx.imgload('grote_ragnar.png')
        self.ragnar = gfx.imgload('ragnar.png')
        self.sprite = self.grote_ragnar
        
        #axe
        self.oncooldown = False
        self.timer = 0
        
        
        #coordinaten
        self.x = x
        self.y = y
        self.xspd = 0
        self.yspd = 0
        
        #crouch
        self.crouching = False
        
        #movement eigenschappen
        self.jmpspd = settings.jumpspeed
        self.movdir = 0
        self.noymove = 0
        self.flyframes = 0
        self.onground = True

        #hitbox rectangle
        width = self.sprite.get_width()
        height = self.sprite.get_height()
        self.hitbox = pygame.Rect(x, y, width, height)

        #dit is de zoekrange voor objecten om collision mee te doen
        #de Inrange is de lijst van objecten die zich binnen 200 pixels van de hero bevinden
        #en waar we dus mee kunnen colliden
        self.xrange = settings.xrange
        self.yrange = settings.yrange

    def predraw(self):
        #we gummen onzelf uit en dan na de movement tekenen we onszelf weer
        gfx.drawrect(settings.background_color, self.x ,self.y, self.hitbox.width, self.hitbox.height)
        
    def bijlgooi(self):
        if globale_variablen.keys[pygame.K_x] and not self.oncooldown:
            objects.hakbijl(self.x, self.y)
            self.oncooldown = True
            self.timer = 0
            
        if self.oncooldown:
            self.timer += 1
            
        if self.timer > settings.cooldown:
            self.oncooldown = False
            
    def crouch(self, collisionrange):
        #crouch
        if globale_variablen.keys[pygame.K_s] and self.crouching == False:
            self.crouching = True
            self.y += settings.gridsize
            self.hitbox.height -= settings.gridsize
            #self.wy = self.wy + self.height
            if self.hitbox.height <= settings.gridsize:
                self.hitbox.height = settings.gridsize
            self.sprite = self.ragnar
        
        #uncrouch
        elif self.crouching == True and not globale_variablen.keys[pygame.K_s]:
            headroom = True
            vierkant = pygame.Rect(self.hitbox.x, self.hitbox.y - settings.gridsize, self.hitbox.width, self.hitbox.height)
            for each in collisionrange:
                if each.hitbox.colliderect(vierkant):
                    headroom = False
            if headroom:
                self.crouching = False                
                self.sprite = self.grote_ragnar
                self.y -= settings.gridsize
                width = self.sprite.get_width()
                height = self.sprite.get_height()
                self.hitbox = pygame.Rect(self.x, self.y, width, height)



    def horizontalmovement(self):    
        #keys[pygame.K_] geeft 0 of 1 als het is ingedrukt of niet
        # als we dus beide waarden bij elkaar optellen met de waarde van a negatief
        #dan krijgen we -1 als we links indrukken, 0 als we beide indrukken en 1 als we recht indrukken
        direction = globale_variablen.keys[pygame.K_d] - globale_variablen.keys[pygame.K_a]
        self.xspd += direction * settings.acceleration
        
        if not self.xspd == 0:
            #friction
            lostspeed = funcs.sign(self.xspd) * settings.friction
            if abs(lostspeed) > abs(self.xspd):
                lostspeed = self.xspd
            self.xspd -= lostspeed
        
        if abs(self.xspd) > settings.maxspeed:
            self.xspd = direction*settings.maxspeed
            
     
    def verticalmovement(self):
        #noymove is gelijk aan het aantal frames dat we niet verticaal bewegen
        #twee frames niet verticaal bewegen is een betrouwbare manier om te checken of we de grond hebben aangeraakt
        if globale_variablen.keys[pygame.K_w] and self.noymove >= 2:
            self.yspd = -self.jmpspd   

    def get_inrange(self):
        #als eerste bepalen we welke objecten dichtbij zijn.
        #dit doen we om het gebruik van rect.collide te minimaliseren zodat het programma efficienter wordt        
        inrangelist = list()
        for each in globale_variablen.allCollisionObjects:
            deltax = abs(each.hitbox.centerx - self.hitbox.centerx) #abs geeft de absolute waarde.
            deltay = abs(each.hitbox.centery - self.hitbox.centery) #dit rekend dus de afstanden tussen de objecten uit
            
            inrange = deltax < self.xrange and deltay < self.yrange 
            if inrange:
                inrangelist.append(each)
        
        return inrangelist
        
    def collision(self, collisionlist):
        #hier wordt xspd en yspd definitief
        #veranderingen hieraan moeten dus hiervoor gebeuren
        
        
        #horizontale collision
        self.x += self.xspd
        self.hitbox.x = self.x
        #muur is een tijdelijke naam voor het object waar we horizontaal tegenaankomen
        muur = False
        for each in collisionlist:
            if self.hitbox.colliderect(each.hitbox):
                muur = each
        #als we niks raken met colliderect blijft muur dus False
        if muur:
            #we verplaatsen ons naar de linker of rechterkant van het object afhankelijk van de bewegingsrichting
            direction = funcs.sign(self.xspd)
            if direction == 1:
                self.hitbox.right = muur.hitbox.left
            if direction == -1:
                self.hitbox.left = muur.hitbox.right
            
            #nu staat de hitbox op de juiste plek en moeten we het karakter even meenemen
            self.x = self.hitbox.x
            #snelheid wordt ook 0 omdat we ergens tegenaan botsen
            self.xspd = 0

            
        #nu komt de verticale collision
        self.y += self.yspd
        self.hitbox.y = self.y
        #grond dient zelfde funcite als muur in t vorige stuk
        grond = False
        for each in collisionlist:
            if self.hitbox.colliderect(each.hitbox):
                grond = each
        if grond:
            direction = funcs.sign(self.yspd)
            if direction == 1:
                self.hitbox.bottom = grond.hitbox.top
            if direction == -1:
                self.hitbox.top = grond.hitbox.bottom
            #hitbox meenemen en tot stilstand komen
            self.y = self.hitbox.y
            self.yspd = 0
        
        
    def gravity(self, collisionlist):
        #we beginnen met de assumptie dat we niet op de grond staan
        if self.yspd == 0:
            self.noymove += 1
        else:
            #als we bewegen is het zeker dat we niet op de grond staan
            self.noymove = 0
            self.onground = False
        
        if self.noymove >= 2:
            #als we twee frames niet verticaal bewegen
            #dan staan we waarschijnlijk op de grond
            #maar omdat dit niet zeker is checken we nog eens met collision
            repeated_test = False
            self.hitbox.y += 2
            for each in collisionlist:
                if each.hitbox.colliderect( self.hitbox ):
                    repeated_test = True
            self.onground = repeated_test
            self.hitbox.y -=2
        
        
        
        #flyframes zijn het aantal cheatframes dat we in de lucht hangen
        if self.onground:
            self.flyframes = 0
        else:
            self.flyframes += 1
  
        if (self.flyframes > settings.flyframeslimit and not self.onground) or self.noymove <= 2:
            self.yspd += settings.gravity
  
        #dit systeem doet alleen gravity als je al bepaalde tijd van een blok afbent
        #het is een soort rubberbandjes systeem om platformen makkelijker te maken met een 'grace period'    
        
    def postdraw(self):
        gfx.draw(self.sprite, self.x, self.y)   
        
        
        
def allupdates():
    inrange = globale_variablen.ragnar.get_inrange()
    globale_variablen.ragnar.bijlgooi()
    globale_variablen.ragnar.crouch(inrange)
    globale_variablen.ragnar.horizontalmovement()
    globale_variablen.ragnar.verticalmovement()
    globale_variablen.ragnar.collision(inrange)
    globale_variablen.ragnar.gravity(inrange)
    globale_variablen.ragnar.postdraw()
        
