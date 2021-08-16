import tkinter as tk
import tkinter.messagebox as mb
class CreateWindow(tk.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.newfile = tk.StringVar()
        self.select = tk.IntVar()
        self.protocol("WM_DELETE_WINDOW",self.confirm_delete)
        self.rename_label = tk.Label(self,width=30,text="Создать файл или папку\n(по умолчанию создается папка)")
        self.first_radiobutton = tk.Radiobutton(self,text = 'Создать файл',value=1,variable=self.select)
        self.second_radiobutton = tk.Radiobutton(self, text='Создать папку', value=2, variable=self.select)
        self.lbl = tk.Label(self)
        self.rename_entry = tk.Entry(self,textvariable=self.newfile)
        self.button = tk.Button(self,text = "Создать",command = self.destroy)
        self.rename_label.pack(padx=5,pady=5)
        self.first_radiobutton.pack(padx=5, pady=5)
        self.second_radiobutton.pack(padx=5, pady=5)
        self.rename_entry.pack(padx=20, pady=20)
        self.button.pack(pady=5,ipadx=2,ipady=2)
        self.lbl.pack(padx=5,pady=5)
    def confirm_delete(self):
            message = "Вы уверены, что хотите закрыть это окно?"
            if mb.askyesno(message=message, parent=self):
                self.destroy()
    def open(self):
        self.grab_set()
        self.wait_window()
        newfile = self.newfile.get()
        select = self.select.get()
        if newfile =="":
            mb.showerror("Ошибка","Невозможно создать данные с пустым именем")
            return 0
        spis = [newfile,select]
        return spis