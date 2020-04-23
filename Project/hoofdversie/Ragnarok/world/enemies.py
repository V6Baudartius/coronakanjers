print(__name__)

#standard exit code to prevent use as a program
if __name__ == '__main__':
    errormessage = 'This is a module and should not be run alone'
    print(errormessage)
    #quits if run as script
    from sys import exit
    exit(errormessage)

#------------------------------------------------

from .. import settings as set, globale_variablen as glob, gfx, funcs
from . import objects
import pygame

class achtervolgend_monster(objects.voorgrondobject):
    def __init__(self, x, y, xspd):
        sprite = gfx.imgload('budgetbeer.png')
        super().__init__(x,y,sprite)
        self.yspd = 0
        
    def update(self):
        self.yspd = int( (glob.ragnar.hitbox.centery - self.hitbox.bottom)/8)
        
        if glob.ragnar.x - self.hitbox.x > set.beerfollowdistance:
            self.hitbox.x = glob.ragnar.x - set.beerfollowdistance
        
        
        self.hitbox.x += self.xspd
        
        self.hitbox.y += self.yspd
        
        
        if glob.levend:
            self.hitbox.x += set.monster_speed
            if self.hitbox.colliderect(glob.ragnar.hitbox):
                glob.levend = False
        
class tutorialtrigger():
    def __init__(self):
        glob.allObjects.append(self)
    def postdraw(self):
        pass
    def animation(self):
        pass
    def update(self):
        if glob.ragnar.x > set.budgetbeerspawn and set.budgetbeer:
            achtervolgend_monster(glob.ragnar.x - 1000, glob.ragnar.y)   
            funcs.destroyObject(self)
        


#deze enemy is een work in progress en haalt waarschijnlijk de release niet
class enemy_lopend():
    def __init__(self, x, y):
        self.sprite = imgload('enemy.bmp')
        self.x = x
        self.y = y
        width = self.sprite.get_width()
        height = self.sprite.get_height()
        self.hitbox = pygame.Rect(x,y,width,height)
        self.direction = 1
        self.speed = 4
    
    def predraw(self):
        gfx.drawrect(settings.background_color,self.x,self.y)
    
    def movementupdate(self):
        self.hitbox.x = self.x                   
        self.hitbox.y = self.y


        if self.direction == 1:
            test_x = self.hitbox.right + self.speed
        elif self.direction == -1:    
            test_x = self.hitbox.left + self.speed*-1
        
        test_pos = (test_x, self.y-50)
        global allCollisionObjects
        
        for each in allCollisionObjects:
        
            if each.hitbox.collidepoint(test_pos):
                self.direction *= -1
                

        self.x += self.speed*self.direction
        
        
        
    def postdraw(self):
        draw(self.sprite, self.x, self.y)