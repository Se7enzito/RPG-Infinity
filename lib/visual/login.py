import tkinter as tk
import tkinter.font as tkFont
from lib.visual.personalizao import personalizacao
from lib.apis.dbAPI import Conexao

class login:
    def __init__(self, root):
        self.root = root

        #setting title
        root.title("Tela de Login")
        #setting window size
        width=650
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
        # GLineEdit_908["show"] = "undefined"

        GLineEdit_530=tk.Entry(root)
        GLineEdit_530["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_530["font"] = ft
        GLineEdit_530["fg"] = "#333333"
        GLineEdit_530["justify"] = "center"
        GLineEdit_530["text"] = "Senha"
        GLineEdit_530.place(x=400,y=275,width=70,height=30)
        GLineEdit_530["show"] = "*"

        GLineEdit_842=tk.Entry(root)
        GLineEdit_842["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_842["font"] = ft
        GLineEdit_842["fg"] = "#333333"
        GLineEdit_842["justify"] = "center"
        GLineEdit_842["text"] = "User"
        GLineEdit_842.place(x=300,y=275,width=70,height=30)
        # GLineEdit_842["show"] = "undefined"

        GButton_377=tk.Button(root)
        GButton_377["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_377["font"] = ft
        GButton_377["fg"] = "#000000"
        GButton_377["justify"] = "center"
        GButton_377["text"] = "Logar"
        GButton_377.place(x=300,y=340,width=70,height=30)
        GButton_377["command"] = self.GButton_377_command

        self.GLineEdit_842 = GLineEdit_842
        self.GLineEdit_530 = GLineEdit_530
        self.GLineEdit_908 = GLineEdit_908

        GMessage_12=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_12["font"] = ft
        GMessage_12["fg"] = "#333333"
        GMessage_12["justify"] = "center"
        # GMessage_12["text"] = "Algum dado esta incorreto"
        GMessage_12["text"] = ""
        GMessage_12.place(x=260,y=140,width=150,height=50)

        self.GMessage_12 = GMessage_12

    def GButton_377_command(self):
        print("Sistema para logar")

        conn = Conexao('lib/db/database.db')
        users = conn.consultar_users_existentes()

        esta_logado = False

        user = self.GLineEdit_842.get()
        senha = self.GLineEdit_530.get()
        nome = self.GLineEdit_908.get()

        if (user in users):
            # print("User foi identificado dentro do banco de dados")

            dados_user = conn.consultar_user(user)
            
            if (dados_user[1] == nome and dados_user[3] == senha):
                esta_logado = True
                # print("Todos os dados estão corretos")
            else:
                # print("Algum dado esta incorreto")
                self.GMessage_12.config(text="Alguma dado está incorreto")

            # if (dados_user[1] == nome):
            #     print("O nome está correto com o do user")

            #     if (dados_user[3] == senha):
            #         print("A senha esta correta")
            #         esta_logado = True
            #     else:
            #         print("A senha esta diferente do user")
            #         return
            # else:
            #     print("O nome esta diferente do user")
            #     return
        else:
            # print("User não foi identificado dentro do banco de dados")
            self.GMessage_12.config(text="User não encontrado")
            return
        
        if (esta_logado):
            print("Sistema para abrir a tela de personalizacao")

            self.fechar_tela()

            tk_personalizao = tk.Tk()
            persona = personalizacao(tk_personalizao, user)

            persona.abrir_tela()

    def abrir_tela(self):
        self.root.deiconify()

    def fechar_tela(self):
        # self.root.withdraw()

        self.root.destroy()

if __name__ == "__main__":
    # root = tk.Tk()
    # app = login(root)

    # app.abrir_tela()
    # root.mainloop()
    pass