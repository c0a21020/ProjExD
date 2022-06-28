import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym
    #print(f"{key},osareta")

def key_up(event):
    global key
    key = ""

def main_proc(): #リアルタイム処理であるので引数にeventはいらない
    global cx,cy,mx,my
    
    delta = {"Up":[0,-1],"Down":[0,+1],"Left":[-1,0],"Right":[+1,0],"":[0,0]} #押されているキーkey、値は移動幅リスト「x、y」
    try:
        if maze_bg[my+delta[key][1]][mx+delta[key][0]] == 0:
            my,mx = my+delta[key][1], mx+delta[key][0]
    except:
        pass
    
    cx,cy = mx*80+50, my*80+50
    canvas.coords("tori",cx,cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canvas = tk.Canvas(root, width=1500, height=900, bg="black")   
    canvas.pack()
    maze_bg = mm.make_maze(15,9)
    #print(maze_bg)
    mm.show_maze(canvas, maze_bg)
    tori = tk.PhotoImage(file="fig/8.png")
    cx,cy = 0,0
    canvas.create_image(cx, cy, image=tori, tag="tori")
    
    key = ""
    mx = 1
    my = 1
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    
    main_proc()
    root.mainloop()
