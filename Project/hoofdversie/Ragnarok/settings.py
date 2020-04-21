print(__name__)

#standard exit code to prevent use as a program
if __name__ == '__main__':
    errormessage = 'This is a module and should not be run alone'
    print(errormessage)
    #quits if run as script
    from sys import exit
    exit(errormessage)

#------------------------------------------------

import pygame

#scherm
scherm_hoogte = 800
scherm_wijdte = 1500
fullscreen = False  #-- fullscreen overschrijft scherm_hoogte en scherm_wijdte
caption = 'RAGNAROK'

#draw
gridsize = 128
scale = 1
enablecolorkey = True
colorkey = (255,255,255)



#camera boundaries
customsize = False
level_w = 0
level_h = 0
camera_xoffset = 350
camera_yoffset = 400

#movement
gravity = 2
jumpspeed = 40
maxspeed = 20
acceleration = 5
friction = 1
flyframeslimit = 7  #dit is het aantal frames dat player niet valt als hij van een blok afstapt
                    #hogere waardes maken platformen aanzienlijk makkelijker

#afstand waarin gezocht wordt als collision gedaan wordt
xrange = gridsize + 10
yrange = 2*gridsize + 10

#framerate
printfps = True
capfps = True
gamespeed = 60

#font
font = "C:/Windows/Fonts/comicz.TTF"

#draw settigns
background_color = (105, 199, 224)

#bijl
xgooisnelheid = 40
ygooisnelheid = -20
cooldown = 20

#monster
monster_speed = 4




#noten:

#onze eigen modules lijken wel gechain-importeerd kunnen worden:
#als ik a importeer bij b en dan b importeer bij c dan heeft c ook abs
#maar bij externe modules als pygame is dit niet het geval.
