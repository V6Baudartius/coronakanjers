print(__name__)

#standard exit code to prevent use as a program
if __name__ == '__main__':
    errormessage = 'This is a module and should not be run alone'
    print(errormessage)
    #quits if run as script
    from sys import exit
    exit(errormessage)

#------------------------------------------------

from .. import settings as set, globale_variablen, gfx, funcs
from . import enemies
import pygame
from random import randint


#een object zonder collision dat wel getekend wordt
#dit vormt de parent van alle andere objecten
#een object heeft drie functies
    #1 predraw, hier haalt hij zichzelf van de schermsurface af
    #2 update, hier wordt de invload van het object op het spel uitgevoerd
    #3 postdraw, nadat camera gemoved is en updates zijn uitgevoerd tekent het zich weer op de schermsurface
    
class genericobject():
    def __init__(self, x, y, sprite):
        globale_variablen.allObjects.append(self)
        
        wijdte = sprite.get_width()
        hoogte = sprite.get_height()
        
        self.sprite = sprite
        self.hitbox = pygame.Rect(x,y,wijdte,hoogte) #we gebruiken een rectangle omdat het een makkelijke manier is om positiewaarden op te slaan in een variabele
        
    def predraw(self):
        #gfx.drawrect(set.background_color,self.hitbox.x,self.hitbox.y, self.hitbox.x + self.hitbox.width, self.hitbox.y + self.hitbox.height)
        pass
        
    def update(self):
        pass    #de update kan bij elk object apart worden gedefineerd
        
    def animation(self):
        pass
    
    def postdraw(self):
        gfx.draw(self.sprite, self.hitbox.x, self.hitbox.y)
        
#----------------Dit object wordt over de player heengetekend, is verder hetzelfde als genericobject

class voorgrondobject():
    def __init__(self, x, y, sprite):
        globale_variablen.voorgrond.append(self)
        
        wijdte = sprite.get_width()
        hoogte = sprite.get_height()
        
        self.sprite = sprite
        self.hitbox = pygame.Rect(x,y,wijdte,hoogte) #we gebruiken een rectangle omdat het een makkelijke manier is om positiewaarden op te slaan in een variabele
        
    def predraw(self):
        #gfx.drawrect(set.background_color,self.hitbox.x,self.hitbox.y, self.hitbox.x + self.hitbox.width, self.hitbox.y + self.hitbox.height)
        pass
        
    def update(self):
        pass    #de update kan bij elk object apart worden gedefineerd
        
    def animation(self):
        pass
    
    def postdraw(self):
        gfx.draw(self.sprite, self.hitbox.x, self.hitbox.y)

#------------------------------------normale/decoratieve objecten -----------------------------------------------------
class sneeuwblokonder(genericobject):
    def __init__(self, x, y):
        sprite = gfx.imgload('sneeuwblokonder.png')
        super().__init__(x, y, sprite)
        
class deur(genericobject):
    def __init__(self, x, y):
        sprite = gfx.imgload('deur.png')
        super().__init__(x, y, sprite) 
        
class grond(genericobject):
    def __init__(self, x, y):
        sprite = gfx.imgload('grond.png')
        super().__init__(x, y, sprite)    
        
class bloem1(voorgrondobject):
    def __init__(self, x, y):
        sprite = gfx.imgload('bloem1.png')
        super().__init__(x, y, sprite) 

class bloem2(voorgrondobject):
    def __init__(self, x, y):
        sprite = gfx.imgload('bloem2.png')
        super().__init__(x, y, sprite)
        
class bloem3(voorgrondobject):
    def __init__(self, x, y):
        sprite = gfx.imgload('bloem3.png')
        super().__init__(x, y, sprite)
        
class bloem4(voorgrondobject):
    def __init__(self, x, y):
        sprite = gfx.imgload('bloem4.png')
        super().__init__(x, y, sprite)
        
class gras1(voorgrondobject):
    def __init__(self, x, y):
        sprite = gfx.imgload('gras1.png')
        super().__init__(x, y, sprite)
        
class gras2(voorgrondobject):
    def __init__(self, x, y):
        sprite = gfx.imgload('gras2.png')
        super().__init__(x, y, sprite)
        
class gras3(voorgrondobject):
    def __init__(self, x, y):
        sprite = gfx.imgload('gras3.png')
        super().__init__(x, y, sprite) 
        
class wolk(genericobject):
    def __init__(self, x, y):
        sprite = gfx.imgload('wolk.png')
        super().__init__(x, y, sprite) 

class wolkcover(voorgrondobject):
    def __init__(self, x, y):
        sprite = gfx.imgload('wolk.png')
        super().__init__(x, y, sprite) 
        
class ijsblokonder(genericobject):
    def __init__(self, x, y):
        sprite = gfx.imgload('ijsblokonder.png')
        super().__init__(x, y, sprite)

class ijsblokonder2(genericobject):
    def __init__(self, x, y):
        sprite = gfx.imgload('ijsblokonder2.png')
        super().__init__(x, y, sprite)





#-------------------------------------------PARENT VAN OBJECTEN MET ANIMATIE-------------------------------------------
        
class animationobject(genericobject):
    def __init__(self,x,y, sprite):
        self.random = False
        self.animationcounter = 0
        self.currentframe = 0
        self.frame = list()
    #bij de kinderen append je alle frames van de animatie aan deze list
        #self.frame.append('frame1.png')
        #self.frame.append('frame2.png')
        #self.frame.append('frame3.png')
        #enz..
        
        super().__init__(x,y,sprite)
        
        
    def animation(self):
        if self.random:
            self.animationcounter += randint(0,1)
        else:
            self.animationcounter += 1
        
        
        if self.animationcounter >= self.animationspeed:
            self.animationcounter = 0
            self.currentframe += 1
            if self.currentframe >= self.animationsize:
                self.currentframe = 0
            
            self.sprite = self.frame[self.currentframe]
            
#---------------------------------------OBJECTEN MET ANIMATIE-------------------------------------------

class kleine_toorts(animationobject):
    def __init__(self, x, y):
        sprite = gfx.imgload('torch0000.png')
        #animation
        super().__init__(x,y,sprite)
        self.animationspeed = 15    #ticks each frame wil be displayed
        self.animationsize = 4  #amount of frames
        self.random = True
        
        self.frame.append(sprite)
        self.frame.append(gfx.imgload('torch0001.png'))
        self.frame.append(gfx.imgload('torch0002.png'))
        self.frame.append(gfx.imgload('torch0003.png'))
        
    def update(self):
        if randint(1,40) == 1:
            smoke(self.hitbox.x + randint(0,set.gridsize/2),self.hitbox.y + 10)
            


class hakbijl(animationobject):
    def __init__(self,x,y, xspd,yspd):
        sprite = gfx.imgload('bijl1.png')
        #animation
        self.animationspeed = 5    #ticks each frame wil be displayed
        self.animationsize = 4  #amount of frames
        super().__init__(x,y,sprite)
        
        self.xspd = xspd
        self.yspd = yspd
        
        self.frame.append(sprite)
        self.frame.append(gfx.imgload('bijl2.png'))
        self.frame.append(gfx.imgload('bijl3.png'))
        self.frame.append(gfx.imgload('bijl4.png'))
        
        #movement
        
    def update(self):        
        #movement + events
        self.hitbox.x += self.xspd
        self.hitbox.y += self.yspd
        self.yspd += set.gravity
        
        if self.yspd > 50:
            funcs.destroyObject(self)
        
        for each in globale_variablen.allCollisionObjects:
            if each.hitbox.colliderect(self.hitbox):
            
                soort = type(each)
                if soort == doos:
                    funcs.destroyObject(each)
                    
                funcs.destroyObject(self)
        
        
#--------------------------------------SPECIALE OBJECTEN/OBJECTEN MET EEN FUNCTIE---------------------------------------------        
        
class transition(genericobject):
    def __init__(self, x, y):
        sprite = gfx.imgload('hitboxdeur.png')
        super().__init__(x, y, sprite)
        deur(x-64,y-64)

    def update(self):
        if self.hitbox.colliderect(globale_variablen.ragnar.hitbox)and globale_variablen.keys[pygame.K_SPACE]:
            globale_variablen.running = False
            
class tutorialtrigger():
    def __init__(self):
        globale_variablen.allObjects.append(self)
    def postdraw(self):
        pass
    def update(self):
        if globale_variablen.ragnar.x > settings.budgetbeerspawn:
            enemies.enemy_achtervolgend(globale_variablen.ragnar.x - 1000, globale_variablen.ragnar.y)
        
            
      

        
class text():
    def __init__(self, x, y,kleur, text):
        print('text gecreerd')
        globale_variablen.teksten.append(self)
        self.x = x
        self.y = y

        grootte = 25
        default_font = pygame.font.Font(set.font, grootte)
        self.screentext = default_font.render(text, True, kleur)

    def draw(self):
        drawx = self.x - globale_variablen.camera_x
        drawy = self.y - globale_variablen.camera_y
        globale_variablen.screen.blit(self.screentext, (drawx,drawy))

class screentext(text):
    def __init__(self, x, y,kleur, text):
        super().__init__(x, y,kleur, text)

    def draw(self):
        globale_variablen.screen.blit(self.screentext, (self.x,self.y))


            
        
            

        
        
#--------------------------------COLLISOIN PARENT-----------------------------------------------        
        
#een object dat collision heeft met de player
class collisionobject(genericobject):
    def __init__(self, x, y, sprite):    
        globale_variablen.allCollisionObjects.append(self)  #deze regel is het enige verschil met een generic object
                                                            #dit is omdat alle collision vanuit de player gedaan wordt
        super().__init__(x, y, sprite)
        
    
#----------------------------COLLISION OBJECTEN --------------------------------------------------------------------        

class grasblok(collisionobject):
    def __init__(self, x, y):
        sprite = gfx.imgload('grasblok.png')
        #de sprite = 500 bij 100
        #de wijdte en hoogte kan ook anders zijn dan de sprite
        #doe dit door een wijdte of hoogte te hardcoden
        super().__init__(x, y, sprite)
        
class steen(collisionobject):   
    def __init__(self, x, y):
        sprite = gfx.imgload('steen.png')
        #de sprite is 50 bij 100
        super().__init__(x, y, sprite)

class doos(collisionobject):
    def __init__(self, x, y):
        sprite = gfx.imgload('doos.png')
        #sprite = 100 bij 100
        super().__init__(x, y, sprite)
             
class ijs(collisionobject):   
    def __init__(self, x, y):
        sprite = gfx.imgload('ijsblokframe.png')
        super().__init__(x, y, sprite)
        
  
class booster(collisionobject):   
    def __init__(self, x, y):
        sprite = gfx.imgload('speed.png')
        super().__init__(x, y, sprite)
        
class modderblok(collisionobject):   
    def __init__(self, x, y):
        sprite = gfx.imgload('modderblok.png')
        super().__init__(x, y, sprite)
        
class grondsolid(collisionobject):
    def __init__(self, x, y):
        sprite = gfx.imgload('grond.png')
        super().__init__(x, y, sprite)

class ijsblokondersolid(collisionobject):   
    def __init__(self, x, y):
        sprite = gfx.imgload('ijsblokonder.png')
        super().__init__(x, y, sprite)

class ijsblokonder2solid(collisionobject):   
    def __init__(self, x, y):
        sprite = gfx.imgload('ijsblokonder2.png')
        super().__init__(x, y, sprite)

class sneeuwblok(collisionobject):   
    def __init__(self, x, y):
        sprite = gfx.imgload('sneeuwblok.png')
        super().__init__(x, y, sprite)

class sneeuwblokondersolid(collisionobject):   
    def __init__(self, x, y):
        sprite = gfx.imgload('sneeuwblokonder.png')
        super().__init__(x, y, sprite)

class brick(collisionobject):   
    def __init__(self, x, y):
        sprite = gfx.imgload('brick.png')
        super().__init__(x, y, sprite)
        
class solidwolk(collisionobject):   
    def __init__(self, x, y):
        sprite = gfx.imgload('wolkmidden.png')
        super().__init__(x, y, sprite)
        wolkcover(x-47, y-52)

class brickwall(collisionobject):   
    def __init__(self, x, y):
        sprite = gfx.imgload('brickwall.png')
        super().__init__(x, y, sprite)      
        
class normalspike(collisionobject):
    def __init__(self, x, y):
        sprite = gfx.imgload('spike.png')
        super().__init__(x, y, sprite)
        
    def update(self):
        if self.hitbox.colliderect(globale_variablen.ragnar.hitbox):
            if globale_variablen.levend:
                globale_variablen.ragnar.yspd = -30
            globale_variablen.levend = False
            
class downspike(normalspike):
    def __init__(self, x, y):
        super().__init__(x, y, sprite)
        self.sprite = gfx.imgload('downspike.png')
        

#---------------Particles Parent-----------------------------------------------

class particle(genericobject):
    def __init__(self, x, y, sprite):
        self.xspd = 0
        self.yspd = 0
        self.duration = 120
        self.time = 0
        super().__init__(x,y,sprite)
        
    def update(self):
        self.hitbox.x += self.xspd
        self.hitbox.y += self.yspd
        self.time += 1
        if self.time > self.duration:
            funcs.destroyObject(self)
        
#-------------------------------Particles------------------------------------------

class smoke(particle):
    def __init__(self, x, y):
        sprite = gfx.imgload('smoke.png')
        super().__init__(x,y,sprite)
        self.yspd = randint(-3,-1)
        self.duration = randint(110,200)
            
class dirt(particle):
    def __init__(self, x, y, direction=1):
        sprite = gfx.imgload('dirt.png')
        super().__init__(x,y,sprite)
        
        
        
        self.xspd = randint(0,10)*direction
        self.yspd = randint(-5,-3) + int(abs(self.xspd)/2)
        
        self.duration = randint(5,15)
        
        
    def update(self):
        super().update()
        self.xspd -= randint(-1,1)
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
