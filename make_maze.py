size = 31
maze = []
for i in range(size):
    maze.append(list("0" * size))
for i in range(size):
    for j in range(size):
        maze[i][j] = int(maze[i][j])