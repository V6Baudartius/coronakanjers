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
scherm_hoogte = 1000
scherm_wijdte = 1000
fullscreen = True  #-- fullscreen overschrijft scherm_hoogte en scherm_wijdte
caption = 'RAGNAROK'

#fps
printfps = True

#algemeen
gravity = 1
gamespeed = 60
gridsize = 100

#camera boundaries
customsize = False
level_w = 0
level_h = 0


#player
jumpspeed = 25
movementspeed = 10
flyframeslimit = 7  #dit is het aantal frames dat player niet valt als hij van een blok afstapt
                    #hogere waardes maken platformen aanzienlijk makkelijker
#afstand waarin gezocht wordt als collision gedaan wordt
xrange = 500
yrange = 500

#framerate
display_framerate = True        #doet nog niks

#draw settigns
background_color = (105, 199, 224)




#noten:

#onze eigen modules lijken wel gechain-importeerd kunnen worden:
#als ik a importeer bij b en dan b importeer bij c dan heeft c ook abs
#maar bij externe modules als pygame is dit niet het geval.
