import tkinter as tk
import os
import shutil
from ctypes import windll
import tkinter.messagebox as mb
import create_window as crw
import rename_window as rmw
class App(tk.Tk):
    path1 = ""
    path2 = ""
    choosefile = ""
    x=0
    y=0
    def __init__(self):
            super().__init__()
            #Row1
            self.label = tk.Entry(self, width=25)
            self.label.grid(row=0,column=0)
            self.btn1=tk.Button(self,height=1,text = "Создать",width=10,command=self.open_createwindow)
            self.btn1.grid(row=0,column=1,sticky="ensw")
            self.btn2=tk.Button(self,height=1,text ='Удалить',width=10,command=self.del_func)
            self.btn2.grid(row=0,column=2,sticky="ensw")
            self.btn3=tk.Button(self,height=1,text = 'Переименовать',width=10,command=self.open_renamewindow)
            self.btn3.grid(row=0, column=3,sticky="ensw")
            self.btn4=tk.Button(self,height=1,text = 'Копировать', width=10,command = self.copy_func)
            self.btn4.grid(row=0, column=4,sticky="ensw")
            self.btn5=tk.Button(self,height=1,text = 'Переместить',width=10,command=self.move_func)
            self.btn5.grid(row=0, column=5,sticky="nswe")
            #Row 2
            self.first_infopath=tk.Listbox(self,width=63,height=1)
            self.first_infopath.grid(row=1, column=0,columnspan=3)
            self.second_infopath=tk.Listbox(self,width=63,height=1)
            self.second_infopath.grid(row=1, column=3, columnspan=3)
            #Row 3
             #Frame 1
            self.f1 = tk.Frame()
            self.f1.grid(row=2,column=0,columnspan=3,ipady=10)

            self.first_list = tk.Listbox(self.f1, width=60, height=20)
            self.first_list.grid(row=0,column=0)

            self.first_scroll = tk.Scrollbar(self.f1,orient="vertical",command=self.first_list.yview)
            self.first_scroll.grid(row=0,column=1,sticky='ns')
            self.first_list.configure(yscrollcommand=self.first_scroll.set)
             #Frame 2
            self.f2 = tk.Frame()
            self.f2.grid(row=2, column=3, columnspan=3,ipady=10)

            self.second_list = tk.Listbox(self.f2, width=60, height=20)
            self.second_list.grid(row=0, column=0, sticky="news")

            self.second_scroll = tk.Scrollbar(self.f2, orient="vertical", command=self.second_list.yview)
            self.second_scroll.grid(row=0, column=1, sticky='nsw')
            self.second_list.configure(yscrollcommand=self.second_scroll.set)

            #Bind
            self.first_list.bind("<Double-Button-1>", lambda event,list = self.first_list, infopath = self.first_infopath:self.first_stepinto(event,list,infopath))
            self.first_list.bind("<Button-1>", lambda event, f=self.first_list:self.choose(event,f))
            self.second_list.bind("<Double-Button-1>", lambda event,list = self.second_list, infopath = self.second_infopath:self.second_stepinto(event,list,infopath))
            self.second_list.bind("<Button-1>",lambda event, f=self.second_list:self.choose(event,f))
            self.first_list.bind("<KeyPress-c>", lambda event, f=self.copy_func:self.bind_func(event,f))
            self.first_list.bind("<KeyPress-x>", lambda event, f=self.move_func:self.bind_func(event,f))
            self.first_list.bind("<KeyPress-r>", lambda event, f=self.open_renamewindow:self.bind_func(event,f))
            self.first_list.bind("<Delete>", lambda event, f=self.del_func:self.bind_func(event,f))
            self.second_list.bind("<KeyPress-c>", lambda event, f=self.copy_func:self.bind_func(event,f))
            self.second_list.bind("<KeyPress-x>", lambda event, f=self.move_func:self.bind_func(event,f))
            self.second_list.bind("<KeyPress-r>", lambda event, f=self.open_renamewindow:self.bind_func(event,f))
            self.second_list.bind("<Delete>", lambda event, f=self.del_func:self.bind_func(event,f))
            self.first_list.bind("<Button-3>", self.menu)
            self.second_list.bind("<Button-3>", self.menu)
            #FirstShow
            mas1=self.get_drives()
            for i in mas1:
                 self.first_list.insert(tk.END, i)
            mas2 = self.get_drives()
            for i in mas2:
                self.second_list.insert(tk.END,i)

            #Menu
    def bind_func(self,event,func):
        func()
    def menu(self, event):
        global x, y
        self.x = event.x
        self.y = event.y
        self.menu = tk.Menu(tearoff=0)
        self.menu.add_command(label="Переместить", command=self.move_func)
        self.menu.add_command(label="Скопировать", command=self.copy_func)
        self.menu.add_command(label="Удалить", command=self.del_func)
        self.menu.add_command(label="Переименовать", command=self.open_renamewindow)
        self.menu.add_command(label="Создать", command=self.open_createwindow)
        self.menu.add_command(label ="Сортировать", command = self.sort_list)
        self.menu.add_command(label = "Обновить", command = self.update_both)
        self.menu.post(event.x_root, event.y_root)
    def open_renamewindow(self):
     try:
        window = rmw.RenameWindow(self)
        window.grab_set()
        App.renamefile = window.open()
        if App.renamefile ==0:
            return 0
        print(App.renamefile)
        if os.path.exists(App.path1 + App.choosefile):
            source = os.path.join(App.path1,App.choosefile)
            print(source)
            destination = os.path.join(App.path1,App.renamefile)
            print(destination)
            os.rename(source,destination)
        else:
            source = os.path.join(App.path2,App.choosefile)
            print(source)
            destination = os.path.join(App.path2,App.renamefile)
            print(destination)
            os.rename(source, destination)
        self.updatelist(App.path1,self.first_list,self.first_infopath)
        self.updatelist(App.path2,self.second_list,self.second_infopath)
     except PermissionError:
        mb.showerror("Ошибка", "Ошибка доступа")
    def open_createwindow(self):
      try:
        window = crw.CreateWindow(self)
        window.grab_set()
        spis = window.open()
        App.newfile = spis[0]
        if App.newfile ==0:
            return 0
        check = spis[1]
        print(App.newfile)
        if os.path.exists(App.path1 + App.choosefile):
            self.temppath = os.path.join(App.path1,App.newfile)
            self.create_func(self.temppath,check)
            self.updatelist(App.path1, self.first_list, self.first_infopath)
        else:
            self.temppath = os.path.join(App.path2,App.newfile)
            self.create_func(self.temppath,check)
            self.updatelist(App.path2, self.second_list, self.second_infopath)
      except FileExistsError and FileNotFoundError:
          mb.showerror("Ошибка","Невозможно создать файл")
      except PermissionError:
          mb.showerror("Ошибка","Ошибка доступа")
    def checknullpath(self,spis):
        tempspis = []
        i = 0
        while i < len(spis):
            if spis[i] != '':
                tempspis.append(spis[i])
                del spis[i]
            else:
                i += 1
        spis = tempspis
        return spis
    def get_drives(self):
        drives = []
        bitmask = windll.kernel32.GetLogicalDrives()
        letter = ord('A')
        while bitmask > 0:
            if bitmask & 1:
                drives.append(chr(letter) + ':')
            bitmask >>= 1
            letter += 1
        return drives
    def copytree(self,src , dst, symlinks=False, ignore=None):
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks, ignore)
            else:
                shutil.copy2(s, d)
    def copy_func(self):
        try:
            if App.path1!=App.path2:
                if os.path.exists(App.path1 + App.choosefile):
                    filepath = os.path.join(App.path1,App.choosefile)
                    inpath = os.path.join(App.path2,App.choosefile)
                    if os.path.isfile(filepath):
                        shutil.copy(src = filepath, dst = inpath)
                    else:
                        self.copytree(filepath,inpath)
                else:
                    filepath = os.path.join(App.path2,App.choosefile)
                    inpath = os.path.join(App.path1,App.choosefile)
                    if os.path.isfile(filepath):
                        shutil.copy(filepath, inpath)
                    else:
                        self.copytree(filepath, inpath)
                self.updatelist(App.path1, self.first_list, self.first_infopath)
                self.updatelist(App.path2, self.second_list, self.second_infopath)
                print(App.choosefile)
            else:
              mb.showerror("Ошибка", "Выбрана одинаковая директория")

        except FileExistsError:
                    mb.showerror("Ошибка","Такой файл уже существует")
        except PermissionError:
                    mb.showerror("Ошибка","Ошибка доступа")
    def move_func(self):
        try:
            if App.path1!=App.path2 and App.path2!=App.path1:
                if os.path.exists(App.path1 + App.choosefile):
                    filepath = App.path1 + App.choosefile
                    inpath = App.path2
                    shutil.move(filepath, inpath)
                else:
                    filepath = App.path2 + App.choosefile
                    inpath = App.path1
                    shutil.move(filepath, inpath)
                self.updatelist(App.path1, self.first_list, self.first_infopath)
                self.updatelist(App.path2, self.second_list, self.second_infopath)
                print(App.choosefile)
            else:
                mb.showerror("Ошибка", "Выбрана одинаковая директория")
        except FileExistsError:
            mb.showerror("Ошибка", "Такой файл уже существует")
        except PermissionError:
            mb.showerror("Ошибка", "Ошибка доступа")
    def del_func(self):
        try:
            if os.path.exists(App.path1 + App.choosefile):
                temppath = os.path.join(App.path1,App.choosefile)
            else:
                temppath = os.path.join(App.path2,App.choosefile)
            print(App.choosefile)
            print(temppath)
            if os.path.isfile(temppath):
                check = mb.askyesno(title="Вопрос", message="Удалить файл?")
                if check == True:
                    os.remove(temppath)
            else:
                check = mb.askyesno(title="Вопрос", message="Удалить папку?")
                if check == True:
                    shutil.rmtree(temppath)
            self.updatelist(App.path1, self.first_list, self.first_infopath)
            self.updatelist(App.path2, self.second_list, self.second_infopath)
        except PermissionError:
            mb.showerror("Ошибка","Ошибка доступа")
    def create_func(self,source,check):
        if check==1:
            with open(source, 'a'):
                os.utime(source, None)
        else:
            os.mkdir(source)
    def choose(self,event,list):
        file = list.curselection()
        if len(file) > 0:
            App.choosefile = list.get(file[0])
            print(App.choosefile)
            self.label.delete(0,tk.END)
            self.label.insert(0,App.choosefile)
    def sort_list(self):
        def sortByAlphabet(inputStr):
            return inputStr[0]

        if App.path1 != App.path2 and App.path2 != App.path1:
            if os.path.exists(App.path1 + App.choosefile):
                spis = os.listdir(App.path1)
                spis.sort(key=sortByAlphabet)
                self.first_infopath.delete(0, tk.END)
                self.first_infopath.insert(tk.END, App.path1)
                self.first_list.delete(0, tk.END)
                self.first_list.insert(tk.END, "...")
                for i in spis:
                    self.first_list.insert(tk.END, i)
            else:
                spis = os.listdir(App.path2)
                spis.sort(key=sortByAlphabet)
                self.second_infopath.delete(0, tk.END)
                self.second_infopath.insert(tk.END, App.path2)
                self.second_list.delete(0, tk.END)
                self.second_list.insert(tk.END, "...")
                for i in spis:
                    self.second_list.insert(tk.END, i)
    def second_stepinto(self,event,list,infopath):
        path = App.path2
        App.path2 = self.stepinto(path,list,infopath)
    def first_stepinto(self,event,list,infopath):
        path = App.path1
        App.path1 = self.stepinto(path,list,infopath)
    def stepinto(self,path,list,infopath):
        file = list.curselection()
        try:
            if "..." in str(list.get(file)):
                path = self.stepout(path,list,infopath)
                return path
            path = path + str(list.get(file)) + "\\"
            if "." in str(list.get(file)):
                os.startfile(path)
                path = self.stepout(path,list,infopath)
            else:
                self.updatelist(path,list,infopath)
            return path
        except PermissionError and NotADirectoryError:
            mb.showerror("Ошибка", "Ошибка доступа")
            path = self.stepout(path,list,infopath)
            return path
        except FileNotFoundError:
            path = self.stepout(path, list, infopath)
            return path
    def stepout(self,path,list,infopath):
        spis = path.split("\\")
        spis = self.checknullpath(spis)
        if len(spis) <= 1:
            spis.pop()
            path = "\\".join(spis[0:len(spis) - 1])
            mas1 = self.get_drives()
            infopath.delete(0, tk.END)
            list.delete(0, tk.END)
            for i in mas1:
                list.insert(tk.END, i)
        else:
            path = "\\".join(spis[0:len(spis) - 1])+"\\"
            self.updatelist(path,list,infopath)
        print(path)
        return path
    def updatelist(self,path,list,infopath):
        spis = os.listdir(path)
        infopath.delete(0, tk.END)
        infopath.insert(tk.END, path)
        list.delete(0, tk.END)
        list.insert(tk.END,"...")
        for i in spis:
            list.insert(tk.END, i)
    def update_both(self):
        self.updatelist(App.path1, self.first_list, self.first_infopath)
        self.updatelist(App.path2, self.second_list, self.second_infopath)
