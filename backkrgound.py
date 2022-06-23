# 50% video-50% zelf



from inspect import modulesbyfile
from site import USER_SITE
from turtle import width
from xml.dom import UserDataHandler
import pygame, sys
import numpy as np

pygame.init()

wIDTH = 1400
hEIGHT = 760
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15   
CROSS_WIDTH = 25 
SPACE = 55
# rgb: red green blue
RED = (247, 243, 222)
# BG_COLOR = (247, 243, 222)
Line_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

screen = pygame.display.set_mode( (wIDTH, hEIGHT) )
pygame.display.set_caption( 'TIC TAC TOE' )
# screen.fill( BG_COLOR )


# board 
board = np.zeros( (BOARD_ROWS, BOARD_COLS) )

#pygame.draw.line ( screen, RED, (10, 10) (300, 300), 10 )

def draw_lines():
    # 1 horizontal
    pygame.draw.line( screen, Line_COLOR, (400, 300), (1000,300), LINE_WIDTH  )
    # 2 horizontal
    pygame.draw.line( screen, Line_COLOR, (400, 500), (1000,500), LINE_WIDTH  )
   
    # 1 vertical
    pygame.draw.line( screen, Line_COLOR, (600, 100), (600,700), LINE_WIDTH  )
    # 2 vertical
    pygame.draw.line( screen, Line_COLOR, (800, 100), (800,700), LINE_WIDTH  )

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle( screen, CIRCLE_COLOR, (int( col * 400 + 100 ), int( row * 400 + 100 )), CIRCLE_RADIUS, CIRCLE_WIDTH )
            elif board[row] [col] == 2:
                pygame.draw.line( screen, CROSS_COLOR, (col * 400 + SPACE, row * 400 + 400 - SPACE), (col * 400 + 400 - SPACE, row * 400 + SPACE), CROSS_WIDTH )
                pygame.draw.line( screen, CROSS_COLOR, (col * 400 + SPACE, row * 400 + SPACE), (col * 400 + 400 - SPACE, row * 400 + 400 - SPACE), CROSS_WIDTH  )
def mark_square(row, col, player):
    board[row][col] = player 

def available_square(row, col):
    return board[row] [col] == 0

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row] [col] == 0:
                return False 

    return True


draw_lines()

player = 1


Plantimg1 = pygame.image.load('./images/2.png')
Plantimg2 = pygame.image.load('./images/6.png')
Plantimg2 = pygame.transform.smoothscale(Plantimg2, (700, 600)) 
Plantimg2 = pygame.transform.rotate(Plantimg2, -23)
Plantimg3 = pygame.image.load('./images/4.png')
Plantimg3 = pygame.transform.smoothscale(Plantimg3, (650, 550))
Plantimg3 = pygame.transform.rotate(Plantimg3, (-70 ))
Plantimg4 = pygame.image.load('./images/5.png')
Plantimg4 = pygame.transform.smoothscale(Plantimg4, (650, 550))
Plantimg4 = pygame.transform.flip(Plantimg4, True, False)
Plantimg5 = pygame.image.load('./images/1.png')
Plantimg5 = pygame.transform.smoothscale(Plantimg5, (550, 450))
Plantimg6 = pygame.image.load('./images/3.png')
Plantimg6 = pygame.transform.smoothscale(Plantimg6, (550,450))
Plantimg6 = pygame.transform.rotate(Plantimg6, (-30))
Plantimg7 = pygame.image.load('./images/Naamloos.png')
Plantimg7 = pygame.transform.smoothscale(Plantimg7, (550, 450))
Plantimg7 = pygame.transform.rotate(Plantimg7, (-90))


# mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            MouseX = event.pos[0] # x
            MouseY = event.pos[1] # y

            clicked_row=int(MouseY // 400)
            clicked_col=int(MouseX // 400)
            print(board) 


            if available_square( clicked_row, clicked_col ):
                if player == 1:
                    mark_square( clicked_row, clicked_col, 1)
                    player = 2

                elif player == 2:
                    mark_square( clicked_row, clicked_col, 2)
                    player = 1

                draw_figures()

    pygame.display.update()       

    screen.blit(Plantimg1, (-200, -200)) 
    screen.blit(Plantimg3, (-200, 200))
    screen.blit(Plantimg2, (-290, -20 ))
    screen.blit(Plantimg5, (1120, 100))
    screen.blit(Plantimg4, (1070, -100))
    screen.blit(Plantimg7, (1200, 380))
    screen.blit(Plantimg6, (1100, 110))
    
   