import tkinter as tk
from tracemalloc import start
import Maze as mm
from tkinter import messagebox
import random
#import datetime


def key_down(event):
    global key
    key = event.keysym
    #print(f"{key},osareta")

def key_up(event):
    global key
    key = ""
    
    if cx == 1274 and cy == 674: # ゴール判定
        messagebox.showinfo("GOAL", "ゴールしました。")  

def main_proc(): #リアルタイム処理であるので引数にeventはいらない
    global cx,cy,mx,my,size
    delta = {"Up":[0,-1],
            "Down":[0,+1],
            "Left":[-1,0],
            "Right":[+1,0],
            "":[0,0]}#押されているキーkey、値は移動幅リスト「x、y」
    try:
        if maze_bg[my+delta[key][1]][mx+delta[key][0]] == 0:
            my,mx = my+delta[key][1], mx+delta[key][0]
    except:
        pass

    cx,cy = mx*size+24, my*size+24
    canvas.coords("tori",cx,cy)
    
    root.after(100, main_proc)

def enemys():
    global mx,my,enemy_x,enemy_y
    delta = {"Up":[0,-1],
            "Down":[0,+1],
            "Left":[-1,0],
            "Right":[+1,0],
            "":[0,0]}

    while cx != 1274 and cy != 674: #こうかとんがゴールするまで
        enemy_x,enemy_y = mx*size+24, my*size+24
        mx += random.randint(-1,1)
        my += random.randint(-1,1)
        canvas.coords("bird",enemy_x,enemy_y)
        root.after(100, main_proc)
        try:
            if maze_bg[my+delta[key][1]][mx+delta[key][0]] == 0:
                my,mx = my+delta[key][1], mx+delta[key][0]
        except:
            pass
        
    

if __name__ == "__main__":
    root = tk.Tk()
    root.title("空飛ぶこうかとん")
    #begin = datetime.datetime.now()

    canvas = tk.Canvas(root, width=1500, height=900, bg="skyblue")   
    canvas.pack()
    maze_bg = mm.make_maze()
    mm.show_maze(canvas, maze_bg)
    tori = tk.PhotoImage(file="fig/3.png")
    enemy = tk.PhotoImage(file="fig/6.png")
    cx,cy = 0,0
    enemy_x, enemy_y = 0,0 
    canvas.create_image(cx, cy, image=tori, tag="tori")
    canvas.create_image(enemy_x,enemy_y, image=enemy, tag="enemy")
    
    size = 50
    key = ""
    mx = 1
    my = 1

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    
    main_proc()
    enemys()
    Start = tk.Label(text='START', foreground='black', background='#ffaacc')
    Start.place()
    #end = datetime.datetime.now()
    #print(f"所要時間：{(end-begin).seconds}秒かかりました")
    print(cx,cy)
    root.mainloop()
