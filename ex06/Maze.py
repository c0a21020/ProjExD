import random
size = 50

def make_maze():
    yoko = 27
    tate = 15
    XP = [ 0, 1, 0, -1]
    YP = [-1, 0, 1,  0]

    maze_lst = []
    #1
    for y in range(tate):
        maze_lst.append([0]*yoko)
    #2
    for x in range(yoko):
        maze_lst[0][x] = 1
        maze_lst[tate-1][x] = 1
    #3
    for y in range(1, tate-1):
        maze_lst[y][0] = 1
        maze_lst[y][yoko-1] = 1
    #4
    for y in range(2, tate-2, 2):
        for x in range(2, yoko-2, 2):
            maze_lst[y][x] = 1
    #5
    for y in range(2, tate-2, 2):
        for x in range(2, yoko-2, 2):
            if x > 2: rnd = random.randint(0, 2)
            else:     rnd = random.randint(0, 3)
            maze_lst[y+YP[rnd]][x+XP[rnd]] = 1

    return maze_lst

def show_maze(canvas, maze_lst):
    color = ["white", "skyblue","pink"]
    start = 1
    goal_x, goal_y = 26, 14
    for y in range(len(maze_lst)):
        for x in range(len(maze_lst[y])):
            canvas.create_rectangle(x*size, y*size, x*size+size, y*size+size, 
                                    fill=color[maze_lst[y][x]], outline=color[maze_lst[y][x]])
    canvas.create_rectangle(size, size, start*size+size, start*size+size, fill=color[2], outline=color[2])
    canvas.create_rectangle((goal_x-1)*size, (goal_y-1)*size, goal_x*size, goal_y*size, fill=color[2], outline=color[2])