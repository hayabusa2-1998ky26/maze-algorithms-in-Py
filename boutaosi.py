import make_maze as m
import random as r
from make_maze import *
for x in range(m.size):
    for y in range(m.size):
        if x == m.size - 1 or y == m.size - 1 or x == 0 or y == 0:
            m.maze[x][y] = 1
        if x % 2 == 0 and y % 2 == 0:
            m.maze[x][y] = 1
for x in range(m.size):
    for y in range(m.size):
        if not (x == m.size - 1 or y == m.size - 1 or x == 0 or y == 0) and x % 2 == 0 and y % 2 == 0:
            one_more = 1
            while one_more == 1:
                rand = r.randint(1, 4)
                one_more = 0
                if rand == 1:
                    if m.maze[x + 1][y] == 1:
                        one_more = 1
                    else:
                        m.maze[x + 1][y] = 1
                if rand == 2:
                    if m.maze[x - 1][y] == 1:
                        one_more = 1
                    else:
                        if x < 3:
                            m.maze[x - 1][y] = 1
                        else:
                            one_more = 1
                if rand == 3:
                    if m.maze[x][y + 1] == 1:
                        one_more = 1
                    else:
                        m.maze[x][y + 1] = 1
                if rand == 4:
                    if m.maze[x][y - 1] == 1:
                        one_more = 1
                    else:
                        m.maze[x][y - 1] = 1
from screen import *