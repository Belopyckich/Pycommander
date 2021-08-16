import tkinter as tk
import hot_keys_window as hkw
import about_window as abw
import main_window as mw
def menu():
    file = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Меню', menu=file)
    file.add_command(label='Горячие клавиши', command=hotkeys)
    file.add_command(label='Помощь', command=about)
    file.add_separator()
    file.add_command(label='Выход', command=app.destroy)
def hotkeys():
    app = hkw.HotKeysWindow()
    app.title("Горячие клавиши")
    app.mainloop()
def about():
    app = abw.AboutWindow()
    app.title("Справка")
    app.mainloop()
app = mw.App()
menubar = tk.Menu(app)
app.config(menu=menubar)
menu()
app.title("PyCommander")
app.iconbitmap("Pyico.ico")
app.resizable(False,False)
app.mainloop()


