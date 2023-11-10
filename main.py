import tkinter as tk
from lib.visual.inicial import inicial

root = tk.Tk()
app = inicial(root)

app.abrir_tela()
root.mainloop()

# from lib.apis.dbAPI import Conexao

# conn = Conexao('lib/db/database.db')

# dados_user = conn.consultar_personalizacao('bernardin')
# print(dados_user)

# users = conn.consultar_users_existentes()

# print(users)

# if 'bernardin' in users:
#     print("Esta")
# else:
#     print("Não esta")

# if 'gabriel' in users:
#     print("Esta")
# else:
#     print("Não esta")

# conn.criar_user('João', 'joaozin', '123456')

# print(conn.consultar_tabela())