# Conway's Game of Life

This directory contains a simple implementation of Conway's Game of Life.
 
1) Any live cell with fewer than two live neighbours dies, as if by underpopulation.

2) Any live cell with two or three live neighbours lives on to the next generation.

3) Any live cell with more than three live neighbours dies, as if by overpopulation.

4) Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
 
1 is dead
0 is alive
 
step 1
1 1 1 
0 0 0 
1 1 1
 
step 2
1 0 1 
1 0 1 
1 0 1
 
step 3
1 1 1 
0 0 0 
1 1 1
