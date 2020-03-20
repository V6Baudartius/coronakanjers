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

#scherm laden
screen = pygame.display.set_mode((height,width))

#mario inladen  
name = 'mario.bmp'
fullname = os.path.join('data', name)
print(fullname)
mario = pygame.image.load(fullname)
collisionBox = mario.get_rect()
doos = pygame.Rect(50,250,100,300)

#mario coordinaten 
x_mario = 200
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
clockspeed = 60

default_font = pygame.font.Font(None, 40)
game_over = False

background = os.path.join('data', 'achtergrond_groen_blouw.png')
bg = pygame.image.load(background)

read_keys = True

while True:

    #loop
    while not game_over:

        #clock.tick(60)
      
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

            
        #beweegt naar rechts
        if keys[pygame.K_d]:
            x_mario += x_speed
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
        y_mario += y_speed    
        
        if x_mario > 300:
            game_over = True
        
        #scherm vullen om eerdere animaties op te vullen met achtergrond
        screen.blit(bg, (0,0))
        
        #mario tekenen
        screen.blit(mario, (x_mario, y_mario))

        #pygame updaten op veranderingen
        pygame.display.update()
        
    while game_over:   
        screen.blit(bg, (0,0))
            
        go_text = default_font.render("Game over", True, (0 , 0, 0))
        screen.blit(go_text, (300,200))
            
        #input
        keys = pygame.key.get_pressed()
            
        if keys[pygame.K_q]:
            game_over = False
            x_mario = 200
            print(x_mario)
            
        #quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
     
            
        #pygame updaten op veranderingen
        pygame.display.update()
    
 
    
    
   
