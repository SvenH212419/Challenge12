
from turtle import width
import pygame, sys

pygame. init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
# rgb: red green blue
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
Line_COLOR = (23, 145, 135)

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'TIC TAC TOE' )
screen.fill( BG_COLOR )

#pygame.draw.line ( screen, RED, (10, 10) (300, 300), 10 )

def draw_lines():
    # 1 horizontal
    pygame.draw.line( screen, Line_COLOR, (0, 200), (600,200), LINE_WIDTH  )
    # 2 horizontal
    pygame.draw.line( screen, Line_COLOR, (0, 400), (600,400), LINE_WIDTH  )
   
    # 1 vertical
    pygame.draw.line( screen, Line_COLOR, (200, 0), (200,600), LINE_WIDTH  )
    # 2 vertical
    pygame.draw.line( screen, Line_COLOR, (400, 0), (400,600), LINE_WIDTH  )

draw_lines()

# mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()