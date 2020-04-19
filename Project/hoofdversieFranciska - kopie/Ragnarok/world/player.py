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
        self.sprite = gfx.imgload('deur.png')
        
        #coordinaten
        self.x = x
        self.y = y
        self.xspd = 0
        self.yspd = 0

        #movement eigenschappen
        self.jmpspd = settings.jumpspeed
        self.mvmtspd = settings.movementspeed           
        self.movdir = 0
        self.noymove = 0
        self.flyframes = 0
        self.onground = True
        
        #hitbox rectangle
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        self.hitbox = pygame.Rect(x, y, self.width, self.height)

        #dit is de zoekrange voor objecten om collision mee te doen
        #de Inrange is de lijst van objecten die zich binnen 200 pixels van de hero bevinden
        #en waar we dus mee kunnen colliden
        self.xrange = settings.xrange
        self.yrange = settings.yrange

    def predraw(self):
        #we gummen onzelf uit en dan na de movement tekenen we onszelf weer
        gfx.drawrect(settings.background_color,self.x,self.y)

    def crouch(self):
        self.height= self.height / 2
        #self.wy = self.wy + self.height
        if self.height <= 100:
            self.height = 100
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.sprite = gfx.imgload('Ragnar.png')
        if globale_variablen.keys[pygame.K_s]:
            self.crouch()
        else:
            self.uncrouch()

    def uncrouch(self):
        self.sprite = gfx.imgload('deur.png')
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def horizontalmovement(self, keys):    
        #keys[pygame.K_] geeft 0 of 1 als het is ingedrukt of niet
        # als we dus beide waarden bij elkaar optellen met de waarde van a negatief
        #dan krijgen we -1 als we links indrukken, 0 als we beide indrukken en 1 als we recht indrukken
        direction = keys[pygame.K_d] - keys[pygame.K_a]
        self.xspd = direction * self.mvmtspd
        
<<<<<<< Updated upstream
=======
        if abs(self.xspd) > settings.maxspeed:
            self.xspd = direction*settings.maxspeed
     
>>>>>>> Stashed changes
    def verticalmovement(self, keys):
        #noymove is gelijk aan het aantal frames dat we niet verticaal bewegen
        #twee frames niet verticaal bewegen is een betrouwbare manier om te checken of we de grond hebben aangeraakt
        if keys[pygame.K_w] and self.noymove >= 2:
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
            for each in collisionlist:
                collideposition = (self.hitbox.centerx, self.hitbox.bottom + 2)
                if each.hitbox.collidepoint( collideposition ):
                    repeated_test = True
            self.onground = repeated_test
        
        #flyframes zijn het aantal cheatframes dat we in de lucht hangen
        if self.onground:
            self.flyframes = 0
        else:
            self.flyframes += 1
  
        if (self.flyframes > settings.flyframeslimit and not self.onground) or self.noymove <= 2:
            self.yspd += settings.gravity
  
        #dit systeem doet alleen gravity als je al bepaalde tijd van een blok afbent
<<<<<<< Updated upstream
        #het is een soort rubberbandjes systeem om platformen makkelijker te maken met een 'grace period'    

    #def crouch(self):
        #self.height = self.height / 2
        #if self.height <= 100:
        #    self.height = 100
        #self.hitbox = pygame.Rect(self.wx, self.wy, self.width, self.height)
        #self.wy = self.wy + self.height
        #self.sprite = imgload('Ragnar.png')
        #print(self.wy)
        
=======
        #het is een soort rubberbandjes systeem om platformen makkelijker te maken met een 'grace period'          

>>>>>>> Stashed changes
    def postdraw(self):
        gfx.draw(self.sprite, self.x, self.y)   
        
        
        
def allupdates():
    globale_variablen.ragnar.horizontalmovement(globale_variablen.keys)
    globale_variablen.ragnar.verticalmovement(globale_variablen.keys)
    globale_variablen.ragnar.crouch()
    inrange = globale_variablen.ragnar.get_inrange()
    globale_variablen.ragnar.collision(inrange)
    globale_variablen.ragnar.gravity(inrange)
    
        
