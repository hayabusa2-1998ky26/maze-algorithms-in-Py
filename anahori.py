import make_maze as m
import random as r
from make_maze import *
def anahori():
    make_maze()
    for x in range(m.size_y):
        for y in range(m.size_x):
            m.maze[x][y] = 1
    m_x = 1
    m_y = 1
    m.maze[m_x][m_y] = 0
    stop = 0
    i = 0
    while True:
        i += 1
        while True:
            one_more = 1
            while one_more == 1:
                one_more = 0
                rand = r.randint(1, 4)
                if not ((rand == 1 and m_x == m.size_y - 2) or (rand == 2 and m_x == 1) or (rand == 3 and m_y == m.size_x - 2) or (rand == 4 and m_y == 1)):
                    if rand == 1:
                        if m.maze[m_x + 2][m_y] == 1:
                            m.maze[m_x + 1][m_y] = 0
                            m.maze[m_x + 2][m_y] = 0
                            m_x += 2
                        else:
                            one_more = 1
                    if rand == 2:
                        if m.maze[m_x - 2][m_y] == 1:
                            m.maze[m_x - 1][m_y] = 0
                            m.maze[m_x - 2][m_y] = 0
                            m_x -= 2
                        else:
                            one_more = 1
                    if rand == 3:
                        if m.maze[m_x][m_y + 2] == 1:
                            m.maze[m_x][m_y + 1] = 0
                            m.maze[m_x][m_y + 2] = 0
                            m_y += 2
                        else:
                            one_more = 1
                    if rand == 4:
                        if m.maze[m_x][m_y - 2] == 1:
                            m.maze[m_x][m_y - 1] = 0
                            m.maze[m_x][m_y - 2] = 0
                            m_y -= 2
                        else:
                            one_more = 1
                else:
                    one_more = 1
                stop = 0
                if m_x == m.size_y - 2:# 1
                    stop += 1
                else:
                    if m.maze[m_x + 2][m_y] == 0:
                        stop += 1

                if m_x == 1:# 2
                    stop += 1
                else:
                    if m.maze[m_x - 2][m_y] == 0:
                        stop += 1

                if m_y == m.size_x - 2:# 3
                    stop += 1
                else:
                    if m.maze[m_x][m_y + 2] == 0:
                        stop += 1

                if m_y == 1:# 4
                    stop += 1
                else:
                    if m.maze[m_x][m_y - 2] == 0:
                        stop += 1
                if stop == 4:
                    break
            if stop == 4:
                break
        t_x = 0
        t_y = 0
        while True:
            t_x = r.randint(0, m.size_y - 2)
            t_y = r.randint(0, m.size_x - 2)
            if t_x % 2 == 1 and t_y % 2 == 1 and m.maze[t_x][t_y] == 0:
                break
        m_x = t_x
        m_y = t_y
        if i == m.size_x * m.size_y * 3:
            break