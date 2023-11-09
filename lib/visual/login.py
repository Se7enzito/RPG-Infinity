import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=700
        height=700
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_165=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_165["font"] = ft
        GLabel_165["fg"] = "#333333"
        GLabel_165["justify"] = "center"
        GLabel_165["text"] = "Senha"
        GLabel_165.place(x=400,y=250,width=70,height=30)

        GLabel_53=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_53["font"] = ft
        GLabel_53["fg"] = "#333333"
        GLabel_53["justify"] = "center"
        GLabel_53["text"] = "Nome"
        GLabel_53.place(x=200,y=250,width=70,height=30)

        GLabel_845=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_845["font"] = ft
        GLabel_845["fg"] = "#333333"
        GLabel_845["justify"] = "center"
        GLabel_845["text"] = "User"
        GLabel_845.place(x=300,y=250,width=70,height=30)

        GLineEdit_908=tk.Entry(root)
        GLineEdit_908["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_908["font"] = ft
        GLineEdit_908["fg"] = "#333333"
        GLineEdit_908["justify"] = "center"
        GLineEdit_908["text"] = "Nome"
        GLineEdit_908.place(x=200,y=275,width=70,height=30)
        GLineEdit_908["show"] = "undefined"

        GLineEdit_530=tk.Entry(root)
        GLineEdit_530["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_530["font"] = ft
        GLineEdit_530["fg"] = "#333333"
        GLineEdit_530["justify"] = "center"
        GLineEdit_530["text"] = "Senha"
        GLineEdit_530.place(x=400,y=275,width=70,height=30)
        GLineEdit_530["show"] = "undefined"

        GLineEdit_842=tk.Entry(root)
        GLineEdit_842["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_842["font"] = ft
        GLineEdit_842["fg"] = "#333333"
        GLineEdit_842["justify"] = "center"
        GLineEdit_842["text"] = "User"
        GLineEdit_842.place(x=300,y=275,width=70,height=30)
        GLineEdit_842["show"] = "undefined"

        GButton_377=tk.Button(root)
        GButton_377["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_377["font"] = ft
        GButton_377["fg"] = "#000000"
        GButton_377["justify"] = "center"
        GButton_377["text"] = "Registrar"
        GButton_377.place(x=300,y=340,width=70,height=30)
        GButton_377["command"] = self.GButton_377_command

    def GButton_377_command(self):
        print("command")

if __name__ == "__main__":
    # root = tk.Tk()
    # app = App(root)
    # root.mainloop()
    pass