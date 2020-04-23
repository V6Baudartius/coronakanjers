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
beerfollowdistance = 5000
budgetbeerspawn = 2000
budgetbeer_speed = 2



#scherm
scherm_hoogte = 800
scherm_wijdte = 1500
fullscreen = True  #-- fullscreen overschrijft scherm_hoogte en scherm_wijdte
caption = 'RAGNAROK'

#draw
gridsize = 64
scale = 1
enablecolorkey = True
colorkey = (255,0,255)



#camera boundaries
customsize = False
level_w = 0
level_h = 0
camera_xoffset = 500
camera_yoffset = 400

#movement
gravity = 2
jumpspeed = 30
speedlimit = 100
hardspeedcap = 120

#normale h variablen
normalacceleration = 6
normalfriction = 3         #dit is de standaard vertraging
normalmaxspeed = 20

luchtacceleration = 3
luchtfriction = 0
luchtmaxspeed = 20

#speciale ondergronden
ijsacceleration = 1
ijsfriction = 0
ijsmaxspeed = 28
icedduration = 300

sneeuwacceleration =  6
sneeuwfriction = 3
sneeuwmaxspeed = 16

modderblokacceleration = 5
modderblokfriction = 2
modderblokmaxspeed = 8

boosteracceleration = 8
boosterfriction = 1
boostermaxspeed = 40




flyframeslimit = 4  #dit is het aantal frames dat player niet valt als hij van een blok afstapt
                    #hogere waardes maken platformen aanzienlijk makkelijker

#afstand waarin gezocht wordt als collision gedaan wordt
xrange = 5*gridsize + 10
yrange = 5*gridsize + 10

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

#restart
deathtimer = 30 #de tijd dat je jezelf doodziet, voordat ie restart




#noten:

#onze eigen modules lijken wel gechain-importeerd kunnen worden:
#als ik a importeer bij b en dan b importeer bij c dan heeft c ook abs
#maar bij externe modules als pygame is dit niet het geval.
