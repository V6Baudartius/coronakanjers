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

#beer
budgetbeer = True
beerfollowdistance = 2000


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
camera_xoffset = 500
camera_yoffset = 400

#movement
gravity = 2
jumpspeed = 40
speedlimit = 100

hardspeedcap = 120

#normale h variablen
normalacceleration = 4
normalfriction = 1          #dit is de standaard vertraging
normalmaxspeed = 20
normalexceedfriction = 0.50 #de procentuele vertraging die je ondervind als je boven de maxspeed uitkomt

luchtacceleration = 4
luchtfriction = 0
luchtmaxspeed = 10
luchtexceedfriction = 0.30 

#speciale ondergronden
ijsacceleration = 2
ijsfriction = 0
ijsmaxspeed = 10
ijsexceedfriction = 0.30  

modderacceleration = 5
modderfriction = 2
moddermaxspeed = 8
modderexceedfriction = 0.60  

boosteracceleration = 8
boosterfriction = 0
boostermaxspeed = 8
boosterexceedfriction = 0.30  



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
xgooisnelheid = 20
ygooisnelheid = -20
cooldown = 30

#monster
monster_speed = 4




#noten:

#onze eigen modules lijken wel gechain-importeerd kunnen worden:
#als ik a importeer bij b en dan b importeer bij c dan heeft c ook abs
#maar bij externe modules als pygame is dit niet het geval.
