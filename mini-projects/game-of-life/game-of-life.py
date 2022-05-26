#!/usr/bin/env python

#This is a first attempt using non O-O methods

#
# /*
# 1) Any live cell with fewer than two live neighbours dies, as if by underpopulation.
#
# 2) Any live cell with two or three live neighbours lives on to the next generation.
#
# 3) Any live cell with more than three live neighbours dies, as if by overpopulation.
#
# 4) Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
#
# 1 is dead
# 0 is alive
#
# step 1
# 1 1 1
# 0 0 0
# 1 1 1
#
# step 2
# 1 0 1
# 1 0 1
# 1 0 1
#
# step 3
# 1 1 1
# 0 0 0
# 1 1 1
#
# */

import random
import time
from datetime import datetime
from random import choice

random.seed(datetime.now())

from typing import List

LIVE_CELL = 0
DEAD_CELL = 1

game_board = []

#DEFINED FOR LATER
MIN_COLS = 3
MIN_ROWS = 3

#Size of board
X = MIN_COLS
Y = MIN_ROWS

# A function to print the game board in a human-readable format.
def print_game(step:int, board: List):
    print(f"\nStep {step}")

    header = "  "

    for i in range(X):
        header += f"  {str(i)}"
    print(header)

    for count, current_row in enumerate(board) :
        print_row = str(count) + " "
        for cell in current_row :
            if cell == LIVE_CELL:
                print_row += "  L"
            elif cell == DEAD_CELL:
                print_row += "  D"
            else:
                print_row += "  N"
        print(print_row)


#A function that sets the game board to an initial state
def init_game_board() -> List:
    board = [None]*Y
    for y in range(Y):
        board[y] = [None]*X

    return board

def init_random_game_board(seq: List) -> List:
    board = init_game_board()

    print(seq)
    for y in range(Y):
        for x in range(X):
            board[y][x] = choice(seq)



    return board

def count_row(row:List, x: int)-> int:
    live_count = 0

    #FIRST COUNT TWO INLINE
    if x == 0:
        for i in [0, 1]:
            if row[i] == LIVE_CELL:
                live_count += 1

    # FIRST COUNT TWO INLINE
    elif x == X-1:
        for i in [x-2, x-1]:
            if row[i] == LIVE_CELL:
                live_count += 1
    #MIDCOLUMN COUNT 3
    else:
        for i in [x-1, x, x+1]:
            if row[i] == LIVE_CELL:
                live_count += 1

    return live_count

def count_neighbours(board: List, x:int, y:int)->List:
    live_count = 0 # NUMBER OF LIVE NEIGHBOURS

    #COUNT THE ADJCENT ROWS
    #first row count only next
    if y == 0:
        live_count += count_row(board[1], x)
    #last row count only prev
    elif y == Y - 1:
        live_count += count_row(board[y -1], x)
    #middle row count prev and next
    else:
        live_count += count_row(board[y - 1], x)
        live_count += count_row(board[y + 1], x)

    #COUNT CURRENT ROW

    #first column count only next
    if x == 0:
        if board[y][1] == LIVE_CELL:
            live_count += 1
    #last column count only prev
    elif x == X-1:
        if board[y][X-2] == LIVE_CELL:
            live_count += 1
    #middle column count next and prev
    else:

        if board[y][x+1] == LIVE_CELL:
            live_count += 1
        if board[y][x-1] == LIVE_CELL:
            live_count += 1

    return live_count

def play_cell(board: List, x:int, y:int)->int:
    curr_state = board[x][y]
    neighbour_count = count_neighbours(board, x, y)

    # 1) Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    if curr_state == LIVE_CELL and neighbour_count < 2:
        return DEAD_CELL

    #print("2")
    # 2) Any live cell with two or three live neighbours lives on to the next generation.
    if curr_state == LIVE_CELL and (neighbour_count == 2 or neighbour_count == 3):
        return LIVE_CELL

    #print("3")
    # 3) Any live cell with more than three live neighbours dies, as if by overpopulation.
    if curr_state == LIVE_CELL and neighbour_count > 3:
        return DEAD_CELL
    #print("4")

    if curr_state == DEAD_CELL and neighbour_count == 3:
        return LIVE_CELL

    # 5) I assume if it hasn't transitioned it should remain the same
    return curr_state

def play_turn(board: List) -> List:
    tmp_board = init_game_board()

    for y in range(Y): #ROWS
        for x in range(X): #COLS
            tmp_board[y][x] = play_cell(board, x, y)

    return tmp_board



#SET UP OUR GAME BOARD

game_board = init_game_board()

print_game(0, game_board)

game_board = [[DEAD_CELL, DEAD_CELL, DEAD_CELL],
              [LIVE_CELL, LIVE_CELL, LIVE_CELL],
              [DEAD_CELL, DEAD_CELL, DEAD_CELL]]

print_game(1, game_board)

#SINCE THE OUTPUT LOOPS I ONLY DO THIS 3 TIMES TO SHOW THE LOOP
for i in range(2, 4):
    game_board = play_turn(game_board)
    print_game(i, game_board)

X = 5
Y = 5

#33% chance of live cell
game_board = init_random_game_board([LIVE_CELL, DEAD_CELL, DEAD_CELL])
print_game(0, game_board)

for i in range(5):
    game_board = play_turn(game_board)
    print_game(i, game_board)
    time.sleep(5)

#print_game(game_board)


