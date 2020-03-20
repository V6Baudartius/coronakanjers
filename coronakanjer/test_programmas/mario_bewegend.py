#initialise
import pygame
import os, sys
pygame.init()
pygame.display.set_caption("MARIO")

screen = pygame.display.set_mode((700,400))

#mario inladen  
name = 'mario_pixelart.png'
fullname = os.path.join('data', name)
print(fullname)
mario = pygame.image.load(fullname)
x = 0
y = 0


#loop
while True:
    #quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        pass
    x = x + 1
    #draw fase
    
    screen.blit(mario, (x, y))
    pygame.display.update()
    
    
    pass