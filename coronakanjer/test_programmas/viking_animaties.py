#initialise
import pygame
import os, sys

pygame.init()
pygame.display.set_caption("MARIO")

screen = pygame.display.set_mode((700,400))
ld = pygame.image.load
ldr = os.path.join
data = 'data'
walkRight = [ld(ldr(data,'R1.png')), ld(ldr(data,'R2.png')), ld(ldr(data,'R3.png')), ld(ldr(data,'R4.png')), ld(ldr(data,'R5.png')), ld(ldr(data,'R6.png')), ld(ldr(data,'R7.png')), ld(ldr(data,'R8.png')), ld(ldr(data,'R9.png'))]
#walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
walkLeft = [ld(ldr(data,'L1.png')), ld(ldr(data,'L2.png')), ld(ldr(data,'L3.png')), ld(ldr(data,'L4.png')), ld(ldr(data,'L5.png')), ld(ldr(data,'L6.png')), ld(ldr(data,'L7.png')), ld(ldr(data,'L8.png')), ld(ldr(data,'L9.png'))]
bg = ld(ldr('data','bgd.jpg'))
stil = ld(ldr('data','standing.png'))

#mario coordinaten 
x_mario = 350
y_mario = 200

#snelheden
x_speed = 5
y_speed = 0
jump_speed = -10

#Y coordinaat van de grond
ground = 300

#de zwaartekracht
gravity = 1

#snelheid van het programma
clock = pygame.time.Clock()
clockspeed = 27

right = False
left = False 

def redrawWindow():
    global WalkCount
    screen.blit(bg, (0,0))
    
    if WalkCount +1 >= 27:
        WalkCount = 0

    if right:
        screen.blit(walkRight[WalkCount//3], (x_mario, y_mario))
        WalkCount += 1

    elif left:
        screen.blit(walkLeft[WalkCount//3], (x_mario, y_mario))
        WalkCount += 1

    else:
        screen.blit(stil, (x_mario, y_mario))




    pygame.display.update()
    



#loop
while True:

    clock.tick(clockspeed)
    
    #quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        pass
    
    #input
    keys = pygame.key.get_pressed()
    
    #beweegt naar links
    if keys[pygame.K_a]:
        x_mario -= x_speed
        right = False
        left = True
        
    #beweegt naar rechts
    elif keys[pygame.K_d]:
        x_mario += x_speed
        right = True
        left = False
    else:
        right = False
        left = False 
        WalkCount = 0
        
    #kijken of mario in delucht zit, zo ja increase de y_speed
    if y_mario < ground:
        y_speed += gravity
    
    #kijken of mario onder de grond is, zo ja maak y_speed 0 en teleporteer mario op de grond
    elif y_mario > ground:
        y_speed = 0
        y_mario = ground
    
    #detecteert of 'w' is ingedrukt en maakt y_speed -10
    if keys[pygame.K_w]:
        y_speed = jump_speed
        
    
    #voert y_speed veranderingen door en laat mario dus bewegen in de y richting    
    y_mario += y_speed    
    

    redrawWindow()
 
    
    
    pass
