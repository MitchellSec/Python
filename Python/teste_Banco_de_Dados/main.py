import sqlite3
conexao = sqlite3.connect('banco_dados.db')

cursor = conexao.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    cpf TEXT UNIQUE NOT NULL
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    quantidade INTEGER NOT NULL
)''')

# IGNORE quando o registro já existe, evitando duplicidade
cursor.execute('''INSERT OR IGNORE INTO usuarios 
    (nome, email, cpf) VALUES 
    ('Maria', 'maria@email.com', '09876543210')''')

cursor.execute('''INSERT INTO produtos 
    (nome, preco, quantidade) VALUES 
    ('Notebook', 3500.00, 10)''')

cursor.execute('''SELECT * FROM usuarios''')
contas = cursor.fetchall()
print (contas)

for conta in contas:
    id, nome, email, cpf = conta
    print(f'''ID: {id}
          Nome: {nome}
          Email: {email}
          CPF: {cpf}''')

conexao.commit()