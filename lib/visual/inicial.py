import tkinter as tk
import tkinter.font as tkFont

class inicial:
    def __init__(self, root):
        root.title("undefined")
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
        print("command")


    def GButton_73_command(self):
        print("command")

if __name__ == "__main__":
    # root = tk.Tk()
    # app = App(root)
    # root.mainloop()
    pass