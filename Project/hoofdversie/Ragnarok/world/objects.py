print(__name__)

#standard exit code to prevent use as a program
if __name__ == '__main__':
    errormessage = 'This is a module and should not be run alone'
    print(errormessage)
    #quits if run as script
    from sys import exit
    exit(errormessage)

#------------------------------------------------

from .. import settings as set, globale_variablen, gfx
import pygame


#een object zonder collision dat wel getekend wordt
#dit vormt de parent van alle andere objecten
#een object heeft drie functies
    #1 predraw, hier haalt hij zichzelf van de schermsurface af
    #2 update, hier wordt de invload van het object op het spel uitgevoerd
    #3 postdraw, nadat camera gemoved is en updates zijn uitgevoerd tekent het zich weer op de schermsurface
    
class genericobject():
    def __init__(self, x, y, width, height, sprite):
        globale_variablen.allObjects.append(self)
        
        self.sprite = sprite
        self.hitbox = pygame.Rect(x,y,width,height) #we gebruiken een rectangle omdat het een makkelijke manier is om positiewaarden op te slaan in een variabele
        
    def predraw(self):
        gfx.drawrect(set.background_color,self.hitbox.x,self.hitbox.y)
        
    def update(self):
        pass    #de update kan bij elk object apart worden gedefineerd
    
    def postdraw(self):
        gfx.draw(self.sprite, self.hitbox.x, self.hitbox.y)

#------------------------------------normale/decoratieve objecten -----------------------------------------------------
        
class kleine_toorts(genericobject):
    def __init__(self, x, y):
        sprite = gfx.imgload('torch.gif')
        width = sprite.get_width()
        height = sprite.get_height()
        super().__init__(x, y, width, height, sprite)
        
    def update(self):
        pass
        
class grond(genericobject):
    def __init__(self, x, y):
        sprite = gfx.imgload('grond.png')
        width = sprite.get_width()
        height = sprite.get_height()
        super().__init__(x, y, width, height, sprite)    
        
        
class spike(genericobject):
    def __init__(self, x, y):
        sprite = gfx.imgload('spike.png')
        width = sprite.get_width()
        height = sprite.get_height()
        super().__init__(x, y, width, height, sprite)
        
    def update(self):
        if self.hitbox.colliderect(globale_variablen.ragnar.hitbox):
            print('dood')
        
        
        
        
        
        
        
        

        
        
        
#--------------------------------------SPECIALE OBJECTEN/OBJECTEN MET EEN FUNCTIE---------------------------------------------        
        
class transition(genericobject):
    def __init__(self, x, y):
        sprite = gfx.imgload('deur.png')
        width = sprite.get_width()
        height = sprite.get_height()
        super().__init__(x, y, width, height, sprite)

    def update(self):
        if self.hitbox.colliderect(globale_variablen.ragnar.hitbox)and globale_variablen.keys[pygame.K_SPACE]:
            globale_variablen.running = False
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#--------------------------------COLLISOIN PARENT-----------------------------------------------        
        
#een object dat collision heeft met de player
class collisionobject(genericobject):
    def __init__(self, x, y, width, height, sprite):    
        globale_variablen.allCollisionObjects.append(self)  #deze regel is het enige verschil met een generic object
                                                            #dit is omdat alle collision vanuit de player gedaan wordt
        super().__init__(x,y,width,height,sprite)
        
       
        #de variablen lokaal opslaan
        self.sprite = sprite
        self.hitbox = pygame.Rect(x, y, width, height)    #deze rectangle wordt gebruikt voor collision, het is de 'hitbox'
        #als je x, y, width of heigt nodig hebt dan kan je dat uit de hitbox
                
    
#----------------------------COLLISION OBJECTEN --------------------------------------------------------------------        

class grasblok(collisionobject):
    def __init__(self, x, y):
        sprite = gfx.imgload('grasblok.png')
        #de sprite = 500 bij 100
        #de wijdte en hoogte kan ook anders zijn dan de sprite
        #doe dit door een wijdte of hoogte te hardcoden
        wijdte = sprite.get_width()
        hoogte = sprite.get_height()
        super().__init__(x, y, wijdte, hoogte, sprite)
        
class steen(collisionobject):   
    def __init__(self, x, y):
        sprite = gfx.imgload('steen.png')
        #de sprite is 50 bij 100
        wijdte = sprite.get_width()
        hoogte = sprite.get_height()
        super().__init__(x, y, wijdte, hoogte, sprite)

class doos(collisionobject):
    def __init__(self, x, y):
        sprite = gfx.imgload('doos.png')
        #sprite = 100 bij 100
        wijdte = sprite.get_width()
        hoogte = sprite.get_height()
        super().__init__(x, y, wijdte, hoogte, sprite)
        


        


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
