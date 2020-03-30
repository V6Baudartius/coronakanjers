#initialise
import pygame
import os, sys

#pygame initialiseren i guess
pygame.init()

#caption veranderen links bovenin het scherm naar MARIO
pygame.display.set_caption("MARIO")

#hoogte en breedte van het scherm
height = 700
width = 400

#kleuren
rood = (255,0,0)
lime = (0,255,0)
limegroen = (50,250,50)
blauw = (0,0,255)

#coordinaten van rectangle1
rect1_x_left = 200
rect1_y_top = 100
rect1_width = 300
rect1_height = 200

#scherm laden
screen = pygame.display.set_mode((height,width))

klik = False

while True:
    #positie van muis krijgen en lijst pos(x,y) maken
    pos = pygame.mouse.get_pos()
    #geeft boolean waarde of je muis zich binnen de square bevindt true or false
    insquare = pos[0] > rect1_x_left and pos[0] < rect1_x_left + rect1_width and pos[1] > rect1_y_top and pos[1] < rect1_y_top + rect1_height
    #quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('klik')
            klik = True and insquare 
                       
        if event.type == pygame.MOUSEBUTTONUP:
            print('unklik')
            klik = False
        pass

    klik = klik and insquare 
    pygame.draw.rect(screen, lime if klik else blauw if insquare else rood,  (rect1_x_left, rect1_y_top, rect1_width, rect1_height))
    #if not klik:
        #pygame.draw.rect(screen, rood,  (rect1_x_left, rect1_y_top, rect1_width, rect1_height))
        #if insquare:
            #pygame.draw.rect(screen, blauw,  (rect1_x_left, rect1_y_top, rect1_width, rect1_height))
    #else:
        #pygame.draw.rect(screen, lime,  (rect1_x_left, rect1_y_top, rect1_width, rect1_height))
    pygame.display.update()

klik = True en insquare = True -> klik = True
klik = False en insquare = True -> klik = False
klik = True en insquare = False -> klik = False
klik = False en insquare = False -> klik = False

    
