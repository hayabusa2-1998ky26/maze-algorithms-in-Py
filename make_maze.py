size_x = 31
size_y = 19
maze = []
def make_maze():
    global maze
    maze = []
    for i in range(size_y):
        maze.append(list("0" * size_x))
    for i in range(size_y):
        for j in range(size_x):
            maze[i][j] = int(maze[i][j])