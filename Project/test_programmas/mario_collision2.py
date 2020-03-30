#initialise
import pygame
import os, sys
pygame.init()
pygame.display.set_caption("MARIO")

screen = pygame.display.set_mode((700,400))

#mario inladen  
name = 'mario.bmp'
fullname = os.path.join('data', name)
print(fullname)
mario = pygame.image.load(fullname)
collisionBox = mario.get_rect()
doos = pygame.Rect(50,250,100,300)

#mario coordinaten 
x_mario = 350
y_mario = 200

#snelheden
x_speed = 3
y_speed = 0
jump_speed = -10

#Y coordinaat van de grond
ground = 300

gravity = 1

#loop
while True:
    #quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        pass
    
    #input
    keys = pygame.key.get_pressed()
    
    #beweegt naar links
    if keys[pygame.K_a]:
        collisionBox.x = x_mario - x_speed
        if not doos.colliderect(collisionBox):
            x_mario -= x_speed
        collisionBox.x = x_mario


    #beweegt naar rechts
    if keys[pygame.K_d]:
        collisionBox.x = x_mario + x_speed
        if not doos.colliderect(collisionBox):
            x_mario += x_speed
        collisionBox.x = x_mario

    #doet niks
    if keys[pygame.K_s]:
        pass
    
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
    
    collisionBox.y = y_mario + y_speed
    if not doos.colliderect(collisionBox):
        y_mario += y_speed
    else:
        y_speed = 0
    collisionBox.y = y_mario


    collisionBox.x = x_mario
    collisionBox.y = y_mario    
    
    #move collisionbozx
    
    #collision met doos
    screen.fill((255,255,255))
    if doos.colliderect(collisionBox):
        pygame.draw.rect(screen, (0,0,255), (200,200,250,250))   
        
            
    #draw fase
    
    pygame.draw.rect(screen, (0,255,0), doos)
    
    rectangle = pygame.Rect(0,300,700,500)
    pygame.draw.rect(screen, (0,0,0), rectangle) #ground
    screen.blit(mario, (x_mario, y_mario))
    
    pygame.display.update()
    
    #pygame.draw.rect(screen,(0,255,0),(0,350,700,50))
    
    
    pass