import tkinter as tk
class HotKeysWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.frame = tk.Frame(self)
        self.x_label = tk.Label(self.frame,text="клавиша x = переместить файл",justify = tk.CENTER,width=50).pack(expand=1)
        self.c_label = tk.Label(self.frame,text="клавиша c = скопировать файл",justify = tk.CENTER,width=50).pack(expand=1)
        self.d_label = tk.Label(self.frame, text="клавиша Delete = удалить файл",justify = tk.CENTER,width=50).pack(expand=1)
        self.r_label = tk.Label(self.frame, text="клавиша r = переименовать файл",justify = tk.CENTER,width=50).pack(expand=1)
        self.button = tk.Button(self.frame,text = "Выход",command = self.destroy)
        self.button.pack(pady=5,ipadx=2,ipady=2)
        self.frame.pack()