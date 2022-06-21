import tkinter as tk
import tkinter.messagebox as tkm
from turtle import bgcolor

#ボタンがクリックされた時
def button_click(event):
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo("", f"{num}のボタンがクリックされました")
    entry.insert(tk.END, num)

#「＝」がクリックされた時
def click_e(event):
    eqn = entry.get()
    res = eval(eqn)
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(res))

#「AC」がクリックされた時
def click_c(event):
    entry.delete(0, tk.END)
    #entry.insert(tk.END, "0")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("電卓")     #電卓のウィンドウを作った
    
    #root.geometry("300x500")
    entry = tk.Entry(root,bg="#EBDECF",fg="#9FC9C7",justify="right", width=12, font=("Times New Roman", 30))
    entry.grid(row=0, column=1, columnspan=4)

    r = 1
    c = 1
    for i, num in enumerate([9,8,7,"+",6,5,4,"-",3,2,1,"*",0,"+"], 1):
        button = tk.Button(root, text=str(num),font=("Times New Roman", 30),bg="#FAF2E6")
        button.grid(row=r, column=c, padx=10, pady=10)
        button.bind("<1>", button_click)
        if i%4 == 0:
            r+=1
            c=0
        c+=1
        c1 = c+1

    eqr_b = tk.Button(root,
                text="=",
                font=("Times New Roman", 30),bg="#FFE0F2",fg="#F9AFEC"
                    )   
    eqr_b.bind("<1>", click_e)
    eqr_b.grid(row=r, column=c, padx=10, pady=10)

    clr_b = tk.Button(root,
                text="AC",
                font=("Times New Roman", 25),bg="#DDD3ED",fg="#8384DF"
                    )   
    clr_b.bind("<1>",click_c )
    clr_b.grid(row=r, column=c1, padx=10, pady=10)

    root.mainloop()