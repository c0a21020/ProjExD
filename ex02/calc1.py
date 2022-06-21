import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    num = btn["text"]
    tkm.showinfo("", f"{num}のボタンがクリックされました")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x500")
    root.title("電卓")

    r,c = 0,0
    for num in range(9,-1,-1):
        button = tk.Button(root,text = num ,width = 4,height = 2,font = ("Times New Roman",20))

        button.bind("<1>",button_click)

        button.grid(row=r,column=c)
        c += 1
        if (num-1)%3 == 0:
            r += 1
            c = 0


    root.mainloop()



