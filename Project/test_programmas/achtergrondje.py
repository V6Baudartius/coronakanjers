import pygame
import os
import math
import sys

pygame.init()
speed = 30
pygame.display.set_caption("MARIO")

clock = pygame.time.Clock()
screen = pygame.display.set_mode((700,400))

#mario inladen  
name = 'mario.bmp'
fullname = os.path.join('data', name)
print(fullname)
mario = pygame.image.load(fullname)

background = 'achtergrond_groen_blouw.png'
#bg = pygame.image.load('data', background).convert()

print('uno')
img = pygame.image
print('dos')
ldr = img.load(os.path.join('data', background))
print('tres')
bg = ldr.convert()
print('tequila!')



bgx = 0
bgx2 = bg.get_width()

def redrawWindow():
    screen.blit(bg, (bgx,0))
    screen.blit(bg, (bgx2, 0))

while True:
    clock.tick(speed)
    #quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        pass
        
    if bgx < bg.get_width() * -1:
        bgx = bg.get_width()
    if bgx2 < bg.get_width() * -1:
        bgx2 = bg.get_width()
        
    bgx -= 2
    bgx2 -= 2
    
    print(bgx)
    print(bgx2)
    
    redrawWindow()
    pygame.display.update()
    
