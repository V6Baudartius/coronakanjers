import pygame, math, os, sys
pygame.init()
pygame.font.init()

#scherm inladen
screen = pygame.display.set_mode((700,400))



default_font = pygame.font.Font(None, 25)

#dit is een nieuwe comment
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        pass
    
    
    
    background = os.path.join('data', 'achtergrond_groen_blouw.png')
    mario = pygame.image.load(background)
    screen.blit(mario, (0,0))
    
    #screen.fill((255,255,255))
    
    go_text = default_font.render("Game over", True, (0 , 0, 0))
    screen.blit(go_text, (200,200))
    
   
    pygame.display.update()
