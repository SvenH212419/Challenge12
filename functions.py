import pygame
import sys


# ---------
# FUNCTIONS
# ---------
def draw_lines(screen, LINE_COLOR, SQUARE_SIZE, WIDTH, HEIGHT, LINE_WIDTH):
    # 1 horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE),
                     (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    # 2 horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE),
                     (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)

    # 1 vertical
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0),
                     (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    # 2 vertical
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0),
                     (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)


def draw_figures(screen, board, BOARD_ROWS, BOARD_COLS, CROSS_COLOR, CROSS_WIDTH, CIRCLE_COLOR, CIRCLE_RADIUS, CIRCLE_WIDTH, SQUARE_SIZE, SPACE):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE//2), int(
                    row * SQUARE_SIZE + SQUARE_SIZE//2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE -
                                 SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)


def mark_square(board, row, col, player):
    board[row][col] = player


def available_square(board, row, col):
    return board[row][col] == 0


def is_board_full(board, BOARD_ROWS, BOARD_COLS):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False

    return True


def check_win(screen, board, CROSS_COLOR, CIRCLE_COLOR, HEIGHT, LINE_WIDTH, SQUARE_SIZE, WIDTH, WIN_LINE_WIDTH, BOARD_ROWS, BOARD_COLS, player):
    # vertical win check
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(
                screen, SQUARE_SIZE, CROSS_COLOR, CIRCLE_COLOR, HEIGHT, LINE_WIDTH, col, player)
            return True

    # horizontal win check
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(
                screen, SQUARE_SIZE, CROSS_COLOR, CIRCLE_COLOR, WIDTH, WIN_LINE_WIDTH, row, player)
            return True

    # asc diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(screen, HEIGHT, WIDTH, WIN_LINE_WIDTH,
                          CIRCLE_COLOR, CROSS_COLOR, player)
        return True

    # desc diagonal win chek
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(screen, WIDTH, HEIGHT, WIN_LINE_WIDTH,
                           CROSS_COLOR, CIRCLE_COLOR, player)
        return True

    return False


def draw_vertical_winning_line(screen, SQUARE_SIZE, CROSS_COLOR, CIRCLE_COLOR, HEIGHT, LINE_WIDTH, col, player):
    posX = col * SQUARE_SIZE + SQUARE_SIZE//2

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (posX, 15),
                     (posX, HEIGHT - 15), LINE_WIDTH)


def draw_horizontal_winning_line(screen, SQUARE_SIZE, CROSS_COLOR, CIRCLE_COLOR, WIDTH, WIN_LINE_WIDTH, row, player):
    posY = row * SQUARE_SIZE + SQUARE_SIZE//2

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, posY),
                     (WIDTH - 15, posY), WIN_LINE_WIDTH)


def draw_asc_diagonal(screen, HEIGHT, WIDTH, WIN_LINE_WIDTH,  CIRCLE_COLOR, CROSS_COLOR, player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, HEIGHT - 15),
                     (WIDTH - 15, 15), WIN_LINE_WIDTH)


def draw_desc_diagonal(screen, WIDTH, HEIGHT, WIN_LINE_WIDTH, CROSS_COLOR, CIRCLE_COLOR, player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, 15),
                     (WIDTH - 15, HEIGHT - 15), WIN_LINE_WIDTH)


def restart(screen, board, BG_COLOR, BOARD_ROWS, BOARD_COLS, LINE_COLOR, SQUARE_SIZE, WIDTH, HEIGHT, LINE_WIDTH):
    screen.fill(BG_COLOR)
    draw_lines(screen, LINE_COLOR, SQUARE_SIZE, WIDTH, HEIGHT, LINE_WIDTH)
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0
