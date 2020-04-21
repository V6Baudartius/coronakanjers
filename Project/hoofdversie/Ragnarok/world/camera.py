print(__name__)

#standard exit code to prevent use as a program
if __name__ == '__main__':
    errormessage = 'This is a module and should not be run alone'
    print(errormessage)
    #quits if run as script
    from sys import exit
    exit(errormessage)

#------------------------------------------------

from .. import settings as s, globale_variablen as g


def cameramovement():
    g.camera_x = g.ragnar.hitbox.bottomleft[0] - s.camera_xoffset
    g.camera_y = g.ragnar.hitbox.bottomleft[1] - s.camera_yoffset
    #linkerboundary
    if g.camera_x <= 0:
        g.camera_x = 0
    
    #rechterboundary
    if g.camera_x > s.level_w - s.scherm_wijdte: #-- je doet schermwijdte omdat je wil weten of de rechterkant van het scherm over de grens gaat en niet de linkerkant
        g.camera_x = s.level_w - s.scherm_wijdte
    
    #bovenkant
    if g.camera_y < 0:
        g.camera_y = 0
        
    #onderkant
    if g.camera_y > s.level_h - s.scherm_hoogte:
        g.camera_y = s.level_h - s.scherm_hoogte
        