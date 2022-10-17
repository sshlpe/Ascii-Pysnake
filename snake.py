from random import randint
from asciimatics.screen import Screen
import time
import sys

from files.classes import Board, Snake
from files.save import check_point, max_score
from files.bot import botAI


def draw_game(screen):
    for line in range(board.sizeY):
        for col in range(board.sizeX):
            if board.board[line][col] in 'sS':
                screen.print_at(board.board[line][col], col, line, 2)
            elif board.board[line][col] in 'm':
                screen.print_at('a', col, line, 1)
            else:
                screen.print_at(board.board[line][col], col, line)

def draw_menu(screen):
    h, w = screen.dimensions
    screen.centre('Welcome  to Sssssnake', int(h/2))
    screen.centre('Press Space to play', int(h/2)+2)

def draw_endgame(screen):
    h, w = screen.dimensions
    screen.centre('U ded', int(h/2))
    screen.centre('Press Space to play Again', int(h/2)+2)

def draw_wingame(screen):
    h, w = screen.dimensions
    screen.centre('U win', int(h/2))
    screen.centre('Press Space to play Again', int(h/2)+2)

def run_game(screen):
    global g_state, board, snake, velx, vely
    if g_state == 2:
        g_state = 3
        h, w = screen.dimensions
        board = Board(w, h-10)
        snake = Snake()
        velx = 0
        vely = 0
    if g_state == 3:
        snake.move(velx, vely)
        if not board.set_snake(snake):
            g_state = 4
        else:
            check_point(snake.score())
            if snake.score() == board.sizeX * board.sizeY:
                g_state = 5

def draw(screen):
    screen.clear()
    if g_state == 1:
        draw_menu(screen)
    if g_state in [2,3]:
        draw_game(screen)
    if g_state == 4:
        draw_endgame(screen)
    if g_state == 5:
        draw_wingame(screen)

def update(screen):
    global velx, vely, g_state, bot, circuit
    ev = screen.get_key()
    run_game(screen)

    if ev == ord(' ') and g_state in [1, 4, 5]:
        g_state = 2

    if ev == ord('b') and g_state in [1, 4, 5]:
        g_state = 2
        bot = True

    if ev  == ord('q'):
        return sys.exit()

    if ev in [ord('a'), ord('d'), ord('s'), ord('w')] and g_state == 3:
        bot = False
        if velx != -moves[ev][0] or not vely == -moves[ev][1]:
            velx, vely = moves[ev]

    if ev == ord('b') and g_state == 3:
        bot = True

    if bot:
        vely, velx = botAI(board, snake, velx, vely)
    return 

def demo(screen):
    while True:

        global board, snake
        draw(screen)
        update(screen)
        h, w = screen.dimensions
        screen.centre(f'Score: {snake.score()}', h-6)
        screen.centre(f'Max Score: {max_score()}', h-5)
        if bot:
            player = 'Bot'
        else:
            player = 'User'
        screen.centre(f'Playing: {player}', h-2)
        screen.refresh()
        time.sleep(0.1)

g_state = 1
board = Board(5,5)
snake = Snake()
velx = 0
vely = 0
bot = False
circuit = None

moves = {ord('d'): [1, 0], ord('a'): [-1, 0], ord('w'): [0,-1], ord('s'):[0,+1]}

Screen.wrapper(demo)


