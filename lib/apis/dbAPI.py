import sqlite3 as sql

class Conexao:
    def __init__(self, database: str) -> None:
        self.database = database
        self.connection = None
        self.cursor = None

    def conectar(self) -> bool:
        self.connection = sql.connect(self.database)
        self.cursor = self.connection.cursor()
        return True

    def desconectar(self) -> bool:
        self.connection.close()

    def criar_user(self, name: str, user: str, senha: str, idade: int) -> tuple:
        self.conectar()
        self.cursor.execute("INSERT INTO users (name, user, senha, idade) VALUES (?, ?, ?, ?)", (name, user, senha, idade))
        self.connection.commit()
        self.desconectar()

        return (name, user, senha, idade)
    
    def atualizar_nome(self, id: int, name: str) -> str:
        self.conectar()
        self.cursor.execute("UPDATE users (name) WHERE id = ? VALUES (?)", (id, name))
        self.connection.commit()
        self.desconectar()

        return name

    def apagar_user(self, id: int) -> list:
        self.conectar()
        backup = self.consultar_dado(id)
        self.cursor.execute("DELETE * FROM users WHERE id = ?", (id,))
        self.connection.commit()
        self.desconectar()

        return backup

    def consultar_dado(self, id: int) -> list:
        self.conectar()
        consulta = self.cursor.execute("SELECT * FROM users WHERE id = ?", (id,)).fetchall()
        self.desconectar()

        return consulta
    
    def consultar_user(self, user: str) -> list:
        self.conectar()
        consulta = self.cursor.execute("SELECT * FROM users WHERE user = ?", (user,)).fetchall()
        self.desconectar()

        return consulta[0]
    
    def consultar_personalizacao(self, user: str) -> list:
        self.conectar()
        consulta = self.cursor.execute("SELECT forca, inteligencia, cor_de_pele, cor_de_cabelo, name FROM users WHERE user = ?", (user,)).fetchall()
        self.desconectar()

        return consulta[0]
    
    def atualizar_personalizacao(self, nome, forca, inteligencia, cor_pele, cor_cabelo, user) -> tuple:
        self.conectar()
        self.cursor.execute("UPDATE users SET name=?, forca=?, inteligencia=?, cor_de_pele=?, cor_de_cabelo=? WHERE user=?", (nome, forca, inteligencia, cor_pele, cor_cabelo, user))
        self.connection.commit()
        self.desconectar

        return (nome, forca, inteligencia, cor_pele, cor_cabelo)
    
    def consultar_users_existentes(self) -> list:
        self.conectar()
        consulta = self.cursor.execute("SELECT user FROM users").fetchall()
        self.desconectar()

        usuarios = [user[0] for user in consulta]

        return usuarios

    def limpar_tabela(self) -> None:
        self.conectar()
        self.cursor.execute("DELETE * FROM users")
        self.connection.commit()
        self.desconectar()


    def consultar_tabela(self) -> list:
        self.conectar()
        consulta = self.cursor.execute("SELECT * FROM users").fetchall()
        self.desconectar()

        return consulta
    
    def atualizar_dados() -> tuple:
        pass

if __name__ == "__main__":
    pass