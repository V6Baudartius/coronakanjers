print(__name__)

#standard exit code to prevent use as a program
if __name__ == '__main__':
    errormessage = 'This is a module and should not be run alone'
    print(errormessage)
    #quits if run as script
    from sys import exit
    exit(errormessage)

#------------------------------------------------

from . import funcs, settings
import pygame


#als True dan is er iets runnend
running = False
#als we restarten dan is dit True als False gaan we naar volgend level
restart = False


#het scherm waarop getekend wordt
screen = funcs.scherminitialisatie(settings.scherm_hoogte, settings.scherm_wijdte, settings.caption)

#hieraan wordt ragnar later toegewezen
ragnar = None

#de check of we doodzijn gegaan of niet
levend = True

#de lijsten met objecten
allCollisionObjects = list()
CollisionRange = list()
allObjects = list()
displayupdatelist = list()
voorgrond = list()
teksten = list()

#achtergrond surface om mee te gummen
backgroundsurface = pygame.Surface((settings.gridsize,settings.gridsize))
backgroundsurface.fill(settings.background_color)

#de positie van de camera
camera_x = 0
camera_y = 0

#keysarray, voor globale acces van het keyboard
keys = None