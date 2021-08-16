import tkinter as tk
import tkinter.messagebox as mb
class RenameWindow(tk.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.renamefile = tk.StringVar()

        self.protocol("WM_DELETE_WINDOW",self.confirm_delete)
        self.rename_label = tk.Label(self,width=30,text="Переименовать файл или папку")
        self.rename_entry = tk.Entry(self,textvariable=self.renamefile)
        self.button = tk.Button(self,text = "Переименовать",command = self.destroy)
        self.rename_label.pack(padx=5,pady=5)
        self.rename_entry.pack(padx=20, pady=20)
        self.button.pack(pady=5,ipadx=2,ipady=2)
    def confirm_delete(self):
        message = "Вы уверены, что хотите закрыть это окно?"
        if mb.askyesno(message=message,parent=self):
            self.destroy()
    def open(self):
        self.grab_set()
        self.wait_window()
        renamefile = self.renamefile.get()
        if renamefile =="":
            mb.showerror("Ошибка","Невозможно переименовать данные")
            return 0
        return renamefile