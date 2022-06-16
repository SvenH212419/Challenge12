import pygame, sys

pygame.init()

WIDTH = 1530
HEIGHT = 760
# rgb: red green blue
RED = (247, 243 , 222)

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'TIC TAC TOE')
screen.fill( RED )

Plantimg1 = pygame.image.load('./images/2.png')

# mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()       

    screen.blit(Plantimg1, (-200, -200)) 