print(__name__)

#standard exit code to prevent use as a program
if __name__ == '__main__':
    errormessage = 'This is a module and should not be run alone'
    print(errormessage)
    #quits if run as script
    from sys import exit
    exit(errormessage)

#------------------------------------------------

from . import funcs, settings as set
import pygame


#als True dan is er iets runnend
running = False


#het scherm waarop getekend wordt
screen = funcs.scherminitialisatie()
camerasurface = pygame.Surface((set.scherm_wijdte/set.scale, set.scherm_hoogte/set.scale))

#hieraan wordt ragnar later toegewezen
ragnar = None

#de check of we doodzijn gegaan of niet
player_alive = True

#de lijsten met objecten voor collision
allCollisionObjects = list()
CollisionRange = list()
allObjects = list()
displayupdatelist = list()




#achtergrond surface om mee te gummen
backgroundsurface = pygame.Surface((set.gridsize,set.gridsize))
backgroundsurface.fill(set.background_color)

#de positie van de camera
camera_x = 0
camera_y = 0

#keysarray, voor globale acces van het keyboard
keys = None