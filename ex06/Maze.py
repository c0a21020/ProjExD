import random
size = 50     #１マスの幅

def make_maze():
    yoko = 27         #27×15のマス
    tate = 15
    XP = [ 0, 1, 0, -1]
    YP = [-1, 0, 1,  0]
    maze_lst = []
    
    #1 中身の数字が全部０の多次元リストを生成
    for y in range(tate):
        maze_lst.append([0]*yoko)
    #2　　（壁を作る）マスの最初と最後の行にあたるリストの部分を０→１にする
    for x in range(yoko):
        maze_lst[0][x] = 1
        maze_lst[tate-1][x] = 1
    for y in range(1, tate-1):
        maze_lst[y][0] = 1
        maze_lst[y][yoko-1] = 1
    #３　　（壁を作る）マスの最初と最後の列にあたるリストの部分を０→１にする
    for y in range(2, tate-2, 2):
        for x in range(2, yoko-2, 2):
            maze_lst[y][x] = 1
    #４　　（迷路を作る）壁の内側にランダムで迷路の道をつくる
    for y in range(2, tate-2, 2):
        for x in range(2, yoko-2, 2):
            if x > 2: rnd = random.randint(0, 2)
            else:     rnd = random.randint(0, 3)
            maze_lst[y+YP[rnd]][x+XP[rnd]] = 1

    return maze_lst


def show_maze(canvas, maze_lst):
    color = ["white", "skyblue","pink"] #マスを壁、道、スタート・ゴールで色分けするためのリスト
    start = 1
    goal_x, goal_y = 26, 14

    for y in range(len(maze_lst)):
        for x in range(len(maze_lst[y])):
            canvas.create_rectangle(x*size, y*size, x*size+size, y*size+size, 
                                    fill=color[maze_lst[y][x]], outline=color[maze_lst[y][x]])                           #壁か道でないところであれば水色、迷路の道なら白
    
    canvas.create_rectangle(size, size, start*size+size, start*size+size, fill=color[2], outline=color[2])               #スタート地点をピンクに
    canvas.create_rectangle((goal_x-1)*size, (goal_y-1)*size, goal_x*size, goal_y*size, fill=color[2], outline=color[2]) #ゴール地点をピンクに