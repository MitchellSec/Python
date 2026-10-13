import sqlite3

conexao = sqlite3.connect('banco_dados.db')
cursor = conexao.cursor()

# Criação da tabela de usuários
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    cpf TEXT UNIQUE NOT NULL
)''')

# Criação da tabela de produtos
cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    quantidade INTEGER NOT NULL
)''')

# Inserção de dados na tabela de usuários (ignorando se já existir)
cursor.execute('''INSERT OR IGNORE INTO usuarios 
    (nome, email, cpf) VALUES 
    ('Maria', 'maria@email.com', '09876543210')''')

# Inserção de dados na tabela de produtos
cursor.execute('''INSERT INTO produtos 
    (nome, preco, quantidade) VALUES 
    ('Caderno', 3500.00, 10)''')

# Consulta os usuários cadastrados
cursor.execute('''SELECT * FROM usuarios''')
contas = cursor.fetchall()

# Exibe os resultados no console
for conta in contas:
    eu, nome, email, cpf = conta
    print(f'''ID: {eu}
    Nome: {nome}
    E-mail: {email}
    CPF: {cpf}''')

# Salva as alterações e fecha a conexão
conexao.commit()
conexao.close()