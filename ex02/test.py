print("Hello world")

import tkinter as tk 

root = tk.Tk()
root.title("お試し")
root.geometry("500x200")

label = tk.Label(root, text = "ahaha",font = ("Helvetica",20))
label.pack()

button = tk.Button(root,text = "osuna")
button.pack()

root.mainloop()