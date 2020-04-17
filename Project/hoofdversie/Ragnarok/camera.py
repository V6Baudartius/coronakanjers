print(__name__)

#standard exit code to prevent use as a program
if __name__ == '__main__':
    errormessage = 'This is a module and should not be run alone'
    print(errormessage)
    #quits if run as script
    from sys import exit
    exit(errormessage)

#------------------------------------------------

from . import settings, globale_variablen as g


def cameramovement():
    g.camera_x = g.ragnar.x - 350
    g.camera_y = g.ragnar.y - 200
    if g.camera_x <= 0:
        g.camera_x = 0
    if g.camera_x > 1000: #dit is niet uit te voeren in een verticaal level, daar moet je code schrijven voor camera_y
        g.camera_x = 1000
    if g.camera_y < -300:
        g.camera_y = -300
    if g.camera_y > 400:
        g.camera_y = 400