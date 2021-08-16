import tkinter as tk
class AboutWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.frame = tk.Frame(self)
        self.about_label = tk.Label(self.frame, text= "Для корректного использования программы пожалуйста убедитесь\n"
                                                "что слева сверху в строке состояния указан файл над которым вы хотите \n"
                                                "провести операции.Для создания папки пожалуйста выберите файл правой\n"
                                                "кнопкой мыши и нажмите создать тогда файл или папка создаться в том\n"
                                                "месте в котором вы выбрали файл\n",justify = tk.LEFT).pack(expand=1)
        self.button = tk.Button(self.frame,text = "Выход",command = self.destroy)
        self.button.pack(pady=5,ipadx=2,ipady=2)
        self.frame.pack()