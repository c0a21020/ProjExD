import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    label = tk.Label(root, text="Hello", font=("Times New Roman", 80))
    label.pack()

    root.mainloop()