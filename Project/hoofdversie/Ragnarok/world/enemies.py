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