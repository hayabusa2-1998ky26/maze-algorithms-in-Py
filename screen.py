import make_maze as m
for x in range(m.size_y):
    hyouzi = ""
    for y in range(m.size_x):
        if m.maze[x][y] == 1:
            hyouzi = hyouzi + "■"
        else:
            hyouzi = hyouzi + " "
        hyouzi = hyouzi + " "
    print(hyouzi)