# MODULES
import pygame
import sys
import numpy as np
import functions


# initializes pygame
pygame.init()

# ---------
# CONSTANTS
# ---------
WIDTH = 800
HEIGHT = WIDTH
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH//BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE//3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE//4
# rgb: red green blue
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

# ------
# SCREEN
# ------
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)

# -------------
# CONSOLE BOARD
# -------------
board = np.zeros((BOARD_ROWS, BOARD_COLS))


functions.draw_lines(screen, LINE_COLOR, SQUARE_SIZE,
                     WIDTH, HEIGHT, LINE_WIDTH)

# ---------
# VARIABLES
# ---------
player = 1
game_over = False

# --------
# MAINLOOP
# --------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            clicked_row = int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)

            if functions.available_square(board, clicked_row, clicked_col):

                functions.mark_square(board, clicked_row, clicked_col, player)
                if functions.check_win(screen, board, CROSS_COLOR, CIRCLE_COLOR, HEIGHT, LINE_WIDTH, SQUARE_SIZE, WIDTH, WIN_LINE_WIDTH, BOARD_ROWS, BOARD_COLS, player):
                    game_over = True
                player = player % 2 + 1

                functions.draw_figures(screen, board, BOARD_ROWS, BOARD_COLS, CROSS_COLOR,
                                       CROSS_WIDTH, CIRCLE_COLOR, CIRCLE_RADIUS, CIRCLE_WIDTH, SQUARE_SIZE, SPACE)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                functions.restart(screen, board, BG_COLOR, BOARD_ROWS, BOARD_COLS,
                                  LINE_COLOR, SQUARE_SIZE, WIDTH, HEIGHT, LINE_WIDTH)
                player = 1
                game_over = False

    pygame.display.update()
