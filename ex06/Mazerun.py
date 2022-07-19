import tkinter as tk
import Maze as mm
from tkinter import messagebox
import random
import time


def key_down(event): #keyが押されているときに行われる処理
    global key
    key = event.keysym

def key_up(event): #keyが何も押されていない時の処理
    global key, begin
    key = ""
    
    if cx == 1274 and cy == 674: #こうかとんの座標がゴールの座標と一致した時、
                                 #こうかとんがゴールしたと判定して、ここまでの経過時間をメッセージボックスでプレイヤーに表示する
        end = time.time() - begin
        messagebox.showinfo("GOAL", f"{end}秒かかりました。")  

def main_proc():               #リアルタイム処理であるので引数にevent
    global cx, cy, mx, my, size
    delta = {"Up":[0, -1],      #押されているキーkey、値は移動幅リスト「x、y」
            "Down":[0, +1],
            "Left":[-1, 0],
            "Right":[+1, 0],
            "":[0, 0]}
    try:
        if maze_bg[my + delta[key][1]][mx + delta[key][0]] == 0:    #移動しようとした先が壁だった場合
            my, mx = my + delta[key][1], mx+delta[key][0]
    except:
        pass

    cx, cy = mx*size+24, my*size+24 #こうかとんの座標
    canvas.coords("tori", cx, cy)
    
    root.after(100, main_proc)

'''def enemys():                                #ランダムで迷路内を動く敵の関数
    global mx, my, enemy_x, enemy_y, rdm_x, rdm_y
    delta = {"Up":[0, -1],
            "Down":[0, +1],
            "Left":[-1, 0],
            "Right":[+1, 0],
            "":[0, 0]}

    while cx != 1274 and cy != 674:          #こうかとんがゴールするまで次のことがやりたかった
        print(0)                          #（←実行して関数が動いていることはこれで確認できたが、canvasが開かない...）
        rdm_x = random.randint(-1, 1)        #１、実行されたら、迷路内のランダムな初期位置に敵が出現する
        rdm_y = random.randint(-1, 1)        #２、ランダムに迷路内を動くように敵の位置を変えたかった。
        enemy_x += 50 * rdm_x                 #while文のなかで書けば、ゴールするまで何回もenemy_x,enemy_y変わると思ってたけど、実は違う？
        enemy_y += 50 * rdm_y
        canvas.coords("bird", enemy_x, enemy_y)
        
        try:
            if maze_bg[my + delta[key][1]][mx + delta[key][0]] == 0:
                my, mx = my + delta[key][1], mx + delta[key][0]
        except:
            pass
    
    root.after(100, main_proc)'''


if __name__ == "__main__":
    root = tk.Tk()
    root.title("個人で考えた迷路")
    begin = time.time()

    canvas = tk.Canvas(root, width=1500, height=900, bg="skyblue")   
    canvas.pack()
    maze_bg = mm.make_maze()
    mm.show_maze(canvas, maze_bg)
    tori = tk.PhotoImage(file = "fig/3.png")
    #敵キャラなので一度コメントアウト enemy = tk.PhotoImage(file="fig/6.png")
    cx, cy = 0, 0
    enemy_x, enemy_y,rdm_x,rdm_y = 0, 0, 0, 0 
    canvas.create_image(cx, cy, image=tori, tag="tori")
    #敵キャラなので一度コメントアウト canvas.create_image(enemy_x,enemy_y, image=enemy, tag="enemy")

    size = 50
    key = ""
    mx = 1
    my = 1

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    
    main_proc()
    Start = tk.Label(text='START', foreground='black', background='#ffaacc')
    Start.place()
    #敵キャラの関数なので一度コメントアウト　enemys()
    root.mainloop()
