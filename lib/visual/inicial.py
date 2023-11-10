import tkinter as tk
import tkinter.font as tkFont
from lib.visual.login import login as logando
from lib.visual.registrar import registro as registramento

class inicial:
    def __init__(self, root):
        self.root = root

        root.title("Tela Inicial")
        width=700
        height=700
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_457=tk.Button(root)
        GButton_457["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=10)
        GButton_457["font"] = ft
        GButton_457["fg"] = "#000000"
        GButton_457["justify"] = "center"
        GButton_457["text"] = "Logar"
        GButton_457.place(x=175,y=250,width=70,height=30)
        GButton_457["command"] = self.GButton_457_command

        GButton_73=tk.Button(root)
        GButton_73["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=10)
        GButton_73["font"] = ft
        GButton_73["fg"] = "#000000"
        GButton_73["justify"] = "center"
        GButton_73["text"] = "Registrar"
        GButton_73.place(x=475,y=250,width=70,height=30)
        GButton_73["command"] = self.GButton_73_command

    def GButton_457_command(self):
        print("Sistema para login")

        self.fechar_tela()

        # login = tk.Toplevel(self.root)
        login = tk.Tk()
        logar = logando(login)

        logar.abrir_tela()


    def GButton_73_command(self):
        print("Sistema para registro")

        self.fechar_tela()

        # registro = tk.Toplevel(self.root)
        registro = tk.Tk()
        registrar = registramento(registro)

        registrar.abrir_tela()

    def abrir_tela(self):
        # self.root.mainloop()

        self.root.deiconify()

    def fechar_tela(self):
        # self.root.withdraw()
        
        self.root.destroy()

if __name__ == "__main__":
    # root = tk.Tk()
    # app = inicial(root)

    # app.abrir_tela()
    # root.mainloop()
    pass