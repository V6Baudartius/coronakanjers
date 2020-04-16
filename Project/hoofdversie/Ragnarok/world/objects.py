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


#dit wordt de parentclass van alle objecten waar hero tegenaan kan botsen
class collision():
    def __init__(self, x, y, width, height, sprite):    

        globale_variablen.allCollisionObjects.append(self)     #we voegen het object toe aan de lijst voor collision
        #de variablen lokaal opslaan
        self.sprite = sprite
        self.hitbox = pygame.Rect(x, y, width, height)    #deze rectangle wordt gebruikt voor collision, het is de 'hitbox'
        #als je x, y, width of heigt nodig hebt dan kan je dat uit de hitbox
                
    def update(self):
        gfx.draw(self.sprite, self.hitbox.x, self.hitbox.y)
        
#hier zijn alle individuelen objecten
class grasblok(collision):
    def __init__(self, x, y):
        sprite = gfx.imgload('grasblok.png')
        #de sprite = 500 bij 100
        #de wijdte en hoogte kan ook anders zijn dan de sprite
        #doe dit door een wijdte of hoogte te hardcoden
        wijdte = sprite.get_width()
        hoogte = sprite.get_height()
        super().__init__(x, y, wijdte, hoogte, sprite)
        
class steen(collision):   
    def __init__(self, x, y):
        sprite = gfx.imgload('steen.png')
        #de sprite is 50 bij 100
        wijdte = sprite.get_width()
        hoogte = sprite.get_height()
        super().__init__(x, y, wijdte, hoogte, sprite)

class doos(collision):
    def __init__(self, x, y):
        sprite = gfx.imgload('doos.png')
        #sprite = 100 bij 100
        wijdte = sprite.get_width()
        hoogte = sprite.get_height()
        super().__init__(x, y, wijdte, hoogte, sprite)
