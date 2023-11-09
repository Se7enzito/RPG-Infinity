import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Personalização")
        #setting window size
        width=600
        height=550
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
        GLabel_165["text"] = "Inteligência"
        GLabel_165.place(x=100,y=200,width=70,height=30)

        GLabel_53=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_53["font"] = ft
        GLabel_53["fg"] = "#333333"
        GLabel_53["justify"] = "center"
        GLabel_53["text"] = "Nome"
        GLabel_53.place(x=100,y=100,width=70,height=30)

        GLabel_845=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_845["font"] = ft
        GLabel_845["fg"] = "#333333"
        GLabel_845["justify"] = "center"
        GLabel_845["text"] = "Força"
        GLabel_845.place(x=100,y=150,width=70,height=30)

        GLineEdit_908=tk.Entry(root)
        GLineEdit_908["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_908["font"] = ft
        GLineEdit_908["fg"] = "#333333"
        GLineEdit_908["justify"] = "center"
        GLineEdit_908["text"] = "Nome"
        GLineEdit_908.place(x=170,y=100,width=70,height=30)
        GLineEdit_908["show"] = "undefined"

        GLineEdit_530=tk.Entry(root)
        GLineEdit_530["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_530["font"] = ft
        GLineEdit_530["fg"] = "#333333"
        GLineEdit_530["justify"] = "center"
        GLineEdit_530["text"] = "Inteligência"
        GLineEdit_530.place(x=170,y=200,width=70,height=30)
        GLineEdit_530["show"] = "undefined"

        GLineEdit_842=tk.Entry(root)
        GLineEdit_842["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_842["font"] = ft
        GLineEdit_842["fg"] = "#333333"
        GLineEdit_842["justify"] = "center"
        GLineEdit_842["text"] = "Força"
        GLineEdit_842.place(x=170,y=150,width=70,height=30)
        GLineEdit_842["show"] = "undefined"

        GButton_377=tk.Button(root)
        GButton_377["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_377["font"] = ft
        GButton_377["fg"] = "#000000"
        GButton_377["justify"] = "center"
        GButton_377["text"] = "Atualizar"
        GButton_377.place(x=130,y=350,width=70,height=30)
        GButton_377["command"] = self.GButton_377_command

        GLineEdit_332=tk.Entry(root)
        GLineEdit_332["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_332["font"] = ft
        GLineEdit_332["fg"] = "#333333"
        GLineEdit_332["justify"] = "center"
        GLineEdit_332["text"] = "Cor Pele"
        GLineEdit_332.place(x=170,y=300,width=70,height=30)

        GLabel_931=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_931["font"] = ft
        GLabel_931["fg"] = "#333333"
        GLabel_931["justify"] = "center"
        GLabel_931["text"] = "Sua Cor Cabelo:"
        GLabel_931.place(x=300,y=250,width=100,height=30)

        GLabel_411=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_411["font"] = ft
        GLabel_411["fg"] = "#333333"
        GLabel_411["justify"] = "center"
        GLabel_411["text"] = "Sua Inteligência:"
        GLabel_411.place(x=300,y=200,width=100,height=30)

        GLabel_396=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_396["font"] = ft
        GLabel_396["fg"] = "#333333"
        GLabel_396["justify"] = "center"
        GLabel_396["text"] = "Cor Pele"
        GLabel_396.place(x=100,y=300,width=70,height=25)

        GLabel_380=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_380["font"] = ft
        GLabel_380["fg"] = "#333333"
        GLabel_380["justify"] = "center"
        GLabel_380["text"] = "Cor Cabelo"
        GLabel_380.place(x=100,y=250,width=70,height=25)

        GLabel_988=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_988["font"] = ft
        GLabel_988["fg"] = "#333333"
        GLabel_988["justify"] = "center"
        GLabel_988["text"] = "Sua Cor Pele:"
        GLabel_988.place(x=300,y=300,width=100,height=30)

        GLabel_228=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_228["font"] = ft
        GLabel_228["fg"] = "#333333"
        GLabel_228["justify"] = "center"
        GLabel_228["text"] = "Sua Força:"
        GLabel_228.place(x=300,y=150,width=100,height=30)

        GLabel_308=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_308["font"] = ft
        GLabel_308["fg"] = "#333333"
        GLabel_308["justify"] = "center"
        GLabel_308["text"] = "Seu Nome:"
        GLabel_308.place(x=300,y=100,width=100,height=30)

        GLineEdit_643=tk.Entry(root)
        GLineEdit_643["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_643["font"] = ft
        GLineEdit_643["fg"] = "#333333"
        GLineEdit_643["justify"] = "center"
        GLineEdit_643["text"] = "Cor Cabelo"
        GLineEdit_643.place(x=170,y=250,width=70,height=30)

        GMessage_233=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_233["font"] = ft
        GMessage_233["fg"] = "#333333"
        GMessage_233["justify"] = "center"
        GMessage_233["text"] = "Message"
        GMessage_233.place(x=380,y=100,width=100,height=30)

        GMessage_121=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_121["font"] = ft
        GMessage_121["fg"] = "#333333"
        GMessage_121["justify"] = "center"
        GMessage_121["text"] = "Message"
        GMessage_121.place(x=385,y=300,width=100,height=30)

        GMessage_593=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_593["font"] = ft
        GMessage_593["fg"] = "#333333"
        GMessage_593["justify"] = "center"
        GMessage_593["text"] = "Message"
        GMessage_593.place(x=380,y=150,width=100,height=30)

        GMessage_633=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_633["font"] = ft
        GMessage_633["fg"] = "#333333"
        GMessage_633["justify"] = "center"
        GMessage_633["text"] = "Message"
        GMessage_633.place(x=395,y=250,width=100,height=30)

        GMessage_464=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_464["font"] = ft
        GMessage_464["fg"] = "#333333"
        GMessage_464["justify"] = "center"
        GMessage_464["text"] = "Message"
        GMessage_464.place(x=395,y=200,width=100,height=30)

        GButton_200=tk.Button(root)
        GButton_200["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_200["font"] = ft
        GButton_200["fg"] = "#000000"
        GButton_200["justify"] = "center"
        GButton_200["text"] = "Carregar"
        GButton_200.place(x=360,y=350,width=70,height=30)
        GButton_200["command"] = self.GButton_200_command

    def GButton_377_command(self):
        print("command")


    def GButton_200_command(self):
        print("command")

if __name__ == "__main__":
    # root = tk.Tk()
    # app = App(root)
    # root.mainloop()
    pass