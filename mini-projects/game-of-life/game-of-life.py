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

from typing import List

LIVE_CELL = 0
DEAD_CELL = 1

game_board = []

#Size of board
X = 3
Y = 3

# A function to print the game board nicely for a human.
def print_game(step:int, board: List) :
    print(f"\nStep {step}")

    header = " "

    for i in range(Y):
        header += f"   {str(i)}"

    for count, current_row in enumerate(board) :
        print_row = str(count) + " "
        for cell in current_row :
            if cell == LIVE_CELL:
                print_row += " L"
            elif cell == DEAD_CELL:
                print_row += " D"
            else:
                print_row += " N"
        print(print_row)


#A function that sets the game board to an initial state
def init_game_board() :
    for x in range(X):
        board[x] = [None for y in range(Y)]


def play_turn(board: List):
    #TODO
    return board



#SET UP OUR GAME BOARD



game_board = [[DEAD_CELL, DEAD_CELL, DEAD_CELL],
              [LIVE_CELL, LIVE_CELL, LIVE_CELL],
              [DEAD_CELL, DEAD_CELL, DEAD_CELL]]

print_game(1, game_board)

for i in range(2, 4):
    game_board = play_turn(game_board)
    print_game(i, game_board)


