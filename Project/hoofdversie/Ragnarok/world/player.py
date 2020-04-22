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
from random import randint
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
        self.sprite = gfx.imgload('vikingsrechts0004.png')
        self.movdir = 1
        
        
        #axe
        self.oncooldown = False
        self.timer = 0
        
        
        #animation
        self.animationcounter = 0
        self.currentframe = 0
        
        self.animationspeed = 2    #ticks each frame wil be displayed
        self.animationsize = 14  #amount of frames
        

        #data
        self.stillleft = gfx.imgload('vikinglinksstil.png')
        self.stillright = gfx.imgload('vikingrechtsstil.png')
        
        self.doodlinks = gfx.imgload('doodlinks0000.png')
        self.doodrechts = gfx.imgload('doodrechts0000.png')
        
        self.crouchrechts = gfx.imgload('vikingscrouchrechts.png')
        self.crouchlinks = gfx.imgload('vikingscrouchlinks.png')
        
        self.right = list()
        self.right.append(gfx.imgload('vikingsrechts0004.png'))
        self.right.append(gfx.imgload('vikingsrechts0005.png'))
        self.right.append(gfx.imgload('vikingsrechts0006.png'))
        self.right.append(gfx.imgload('vikingsrechts0007.png'))
        self.right.append(gfx.imgload('vikingsrechts0008.png'))
        self.right.append(gfx.imgload('vikingsrechts0009.png'))
        self.right.append(gfx.imgload('vikingsrechts0010.png'))
        self.right.append(gfx.imgload('vikingsrechts0011.png'))
        self.right.append(gfx.imgload('vikingsrechts0012.png'))
        self.right.append(gfx.imgload('vikingsrechts0013.png'))
        self.right.append(gfx.imgload('vikingsrechts0000.png'))
        self.right.append(gfx.imgload('vikingsrechts0001.png'))
        self.right.append(gfx.imgload('vikingsrechts0002.png'))
        self.right.append(gfx.imgload('vikingsrechts0003.png'))
        
        self.left = list()
        self.left.append(gfx.imgload('viking0004.png'))
        self.left.append(gfx.imgload('viking0005.png'))
        self.left.append(gfx.imgload('viking0006.png'))
        self.left.append(gfx.imgload('viking0007.png'))
        self.left.append(gfx.imgload('viking0008.png'))
        self.left.append(gfx.imgload('viking0009.png'))
        self.left.append(gfx.imgload('viking0010.png'))
        self.left.append(gfx.imgload('viking0011.png'))
        self.left.append(gfx.imgload('viking0012.png'))
        self.left.append(gfx.imgload('viking0013.png'))
        self.left.append(gfx.imgload('viking0000.png'))
        self.left.append(gfx.imgload('viking0001.png'))
        self.left.append(gfx.imgload('viking0002.png'))
        self.left.append(gfx.imgload('viking0003.png'))
        
        #coordinaten
        self.x = x
        self.y = y
        self.xspd = 0
        self.yspd = 0
        
        #crouch
        self.crouching = False
        
        
        #movement eigenschappen
        self.jmpspd = settings.jumpspeed
        self.iced = False
        
        self.noymove = 0
        self.flyframes = 0
        self.onground = True

        #hitbox rectangle
        width = self.sprite.get_width()
        height = self.sprite.get_height()
        self.hitbox = pygame.Rect(x, y, width, height)
        self.grondbox = pygame.Rect(x-20, self.hitbox.bottom , self.hitbox.width+40, 5)

        #dit is de zoekrange voor objecten om collision mee te doen
        #de Inrange is de lijst van objecten die zich binnen 200 pixels van de hero bevinden
        #en waar we dus mee kunnen colliden
        self.xrange = settings.xrange
        self.yrange = settings.yrange

    def predraw(self):
        #we gummen onzelf uit en dan na de movement tekenen we onszelf weer
        #gfx.drawrect(settings.background_color, self.x ,self.y, self.hitbox.width, self.hitbox.height)
        pass
        


        
    def bijlgooi(self):
        if globale_variablen.levend:
            if globale_variablen.keys[pygame.K_x] and not self.oncooldown:
                objects.hakbijl(self.hitbox.centerx, self.y, self.xspd + self.movdir*settings.xgooisnelheid, self.yspd + settings.ygooisnelheid)
                self.oncooldown = True
                self.timer = 0
                
            if self.oncooldown:
                self.timer += 1
                
            if self.timer > settings.cooldown:
                self.oncooldown = False
            
    def crouch(self, collisionrange):
        if globale_variablen.levend:
            #crouch
            if globale_variablen.keys[pygame.K_s] and not self.crouching:
                self.crouching = True
                self.y += settings.gridsize
                self.hitbox.height -= settings.gridsize
            
            #uncrouch
            #als je op wil staan
            elif self.crouching and not globale_variablen.keys[pygame.K_s]:
                #check collision voor hoofdruimte
                headroom = True
                vierkant = pygame.Rect(self.hitbox.x, self.hitbox.y - settings.gridsize, self.hitbox.width, self.hitbox.height)
                for each in collisionrange:
                    if each.hitbox.colliderect(vierkant):
                        headroom = False
                #als er ruimte is 
                if headroom:
                    #sta op
                    self.crouching = False                
                    self.y -= settings.gridsize
                    self.hitbox.y = self.y
                    self.hitbox.height += settings.gridsize
                #zo niet
                else:
                #move naar voren
                    self.xspd = 3
                    
        if self.crouching:
            self.iced = True
                    
    def grondcheck(self, collisionrange):
        self.grondbox.x = self.x
        self.grondbox.y = self.hitbox.bottom

        self.ondergrond = None
        for each in collisionrange:
            if self.grondbox.colliderect(each.hitbox):
                if self.ondergrond == objects.ijs or self.ondergrond == objects.modderblok or self.ondergrond == objects.booster or self.ondergrond == objects.sneeuwblok or self.ondergrond == None:
                        self.ondergrond = type(each)
                        
                        
      
                
                

    def horizontalmovement(self):    
        #ondergrond check
        #air
        if self.ondergrond == None:   
            if not self.iced:
                acceleration = settings.normalacceleration
                friction = settings.normalfriction
            else:
                acceleration = settings.ijsacceleration
                friction = settings.ijsfriction
            maxspeed = settings.luchtmaxspeed

        #ijs
        elif self.ondergrond == objects.ijs:   
            acceleration = settings.ijsacceleration
            friction = settings.ijsfriction
            maxspeed = settings.ijsmaxspeed
            self.iced = True
        elif self.ondergrond == objects.booster:
            acceleration = settings.boosteracceleration
            friction = settings.boosterfriction
            maxspeed = settings.boostermaxspeed
            self.iced = True
        
        #alles wat niet ijs is 
        else: 
            self.iced = False
            
            if self.ondergrond == objects.modderblok:   
                acceleration = settings.modderblokacceleration
                friction = settings.modderblokfriction
                maxspeed = settings.modderblokmaxspeed
                
            elif self.ondergrond == objects.sneeuwblok:   
                acceleration = settings.sneeuwacceleration
                friction = settings.sneeuwfriction
                maxspeed = settings.sneeuwmaxspeed
            
            #normaal
            else:
                acceleration = settings.normalacceleration
                friction = settings.normalfriction
                maxspeed = settings.normalmaxspeed
                
                
        #buikglij assist
        if self.crouching and not friction == 0:
            friction = 1

        
        #accelaration + limiter
        if globale_variablen.levend and not self.crouching :
            #keys[pygame.K_] geeft 0 of 1 als het is ingedrukt of niet
            # als we dus beide waarden bij elkaar optellen met de waarde van a negatief
            #dan krijgen we -1 als we links indrukken, 0 als we beide indrukken en 1 als we recht indrukken
            left = globale_variablen.keys[pygame.K_a]
            right = globale_variablen.keys[pygame.K_d]
            self.direction = right - left
            
            #als we niet op ijs staan doe dan normale acceleratie
            if not self.iced:
                self.xspd += self.direction * acceleration
            
            #als we net ijs hebben aangeraakt versnel dan alleen als we langzaam gaan
            elif abs(self.xspd) < maxspeed:
                self.xspd += self.direction * acceleration
            
            #dit is om te weten welke animatie moet
            if right:       #rechts heeft voorrang over links omdat men naar rechs behoort te bewegen
                self.movdir = 1
            elif left:
                self.movdir = -1
        
        #friction       
        #als de snelheid kleiner is dan de maxspeed
        lostspeed = friction

        #code om te voorkomen dat friction door nul heen gaat
        if abs(lostspeed) > abs(self.xspd):
            lostspeed = abs(self.xspd)

        #en we verliezen de snelheid
        self.xspd -= lostspeed*funcs.sign(self.xspd)

        #dit is de soft cap
        #normaal houden we ons aan de maxspeed
        if not self.iced and abs(self.xspd) > maxspeed:
            self.xspd = funcs.sign(self.xspd)*maxspeed

        #als we ijs hebben aangeraakt deon we dat niet
        else:
            pass
        
        
        #hard cap
        #code om te voorkomen dat we harder gaan dan de game aankan
        if abs(self.xspd) > settings.hardspeedcap:
            self.xspd = self.direction*settings.hardspeedcap
            
     
    def verticalmovement(self):
        if globale_variablen.levend and not self.crouching:
            #noymove is gelijk aan het aantal frames dat we niet verticaal bewegen
            #twee frames niet verticaal bewegen is een betrouwbare manier om te checken of we de grond hebben aangeraakt
            if globale_variablen.keys[pygame.K_w] and self.noymove >= 2:
                 self.yspd = -self.jmpspd
        
        #code om de game te beschermen
        if abs(self.yspd) > settings.hardspeedcap:
            self.yspd = funcs.sign(self.yspd)*settings.hardspeedcap

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
        self.hitbox.y = self.y
        
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
            #als er collision is en snelheid > 60
            if self.yspd > 50:
                #creeer een aantal particles die naar links gaan
                for i in range(randint(10,20)):
                    objects.dirt(self.hitbox.centerx, self.hitbox.bottom, 1)
                #en een paar die naar rechts gaan
                for i in range(randint(10,20)):
                    objects.dirt(self.hitbox.centerx, self.hitbox.bottom, -1)
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
    
    def animation(self):
        #als we dood zijn
        if not globale_variablen.levend:
            #check richting en doe bijbehorendesprite
            if self.movdir == 1:
                self.sprite = self.doodrechts
            else: 
                self.sprite = self.doodlinks
        #als we leven en als we crouchen
        elif self.crouching:
            if self.movdir == 1:
                self.sprite = self.crouchrechts
            else: 
                self.sprite = self.crouchlinks
        #als we staan en stilstaan
        elif self.direction == 0:
            #check richting en doe bijbehorende sprite
            if self.movdir == 1:
                self.sprite = self.stillright
            else: 
                self.sprite = self.stillleft
        #als geen van deze speciale gevallen waar is
        #dan lopen we en treed het oude systeem in werking
        else:
        
            self.animationcounter += 1
            if self.animationcounter >= self.animationspeed:
                self.animationcounter = 0
                self.currentframe += 1
                if self.currentframe >= self.animationsize:
                    self.currentframe = 0
                
                if self.movdir == 1:
                    self.sprite = self.right[self.currentframe]
                else: 
                    self.sprite = self.left[self.currentframe]

    def postdraw(self):
        
        gfx.draw(self.sprite, self.x, self.y)   
        
        
        
def allupdates():
    inrange = globale_variablen.ragnar.get_inrange()
    globale_variablen.ragnar.crouch(inrange)
    globale_variablen.ragnar.bijlgooi()
    globale_variablen.ragnar.grondcheck(inrange)
    globale_variablen.ragnar.horizontalmovement()
    globale_variablen.ragnar.verticalmovement()
    globale_variablen.ragnar.collision(inrange)
    globale_variablen.ragnar.gravity(inrange)
    globale_variablen.ragnar.animation()
    
        
