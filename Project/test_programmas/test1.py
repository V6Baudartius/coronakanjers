import pygame
pygame.init()
pygame.display.set_caption("gametitelcoronapoep")

screen = pygame.display.set_mode((700,400))
run = True
circle_pos_x=350
circle_pos_y=200
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pass

    pygame.draw.circle( screen, (255,0,0), (circle_pos_x,circle_pos_y), 50)
    pygame.display.update()
pygame.quit()
