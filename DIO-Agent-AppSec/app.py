import sqlite3

# Banco de dados local em memória
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Criando tabela e usuário de teste
cursor.execute("""
CREATE TABLE users (
    username TEXT,
    password TEXT
)
""")

cursor.execute(
    "INSERT INTO users VALUES (?, ?)",
    ("admin", "senha123")
)

# Login vulnerável: concatenação direta dos dados
# Login corrigido: consulta parametrizada
def login(username, password):
    query = (
        "SELECT * FROM users "
        "WHERE username = ? AND password = ?"
    )

    print("\nConsulta SQL executada:")
    print(query)

    cursor.execute(query, (username, password))
    return cursor.fetchone() is not None

if __name__ == "__main__":
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if login(usuario, senha):
        print("\nLogin realizado!")
    else:
        print("\nCredenciais inválidas.")

        