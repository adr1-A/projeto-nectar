import sqlite3
import random
from faker import Faker

# Cria uma instância do Faker com localização brasileira
fake = Faker('pt_BR')

# Conecta ao banco de dados SQLite
conn = sqlite3.connect("nectar_db.sqlite")
cursor = conn.cursor()

# Cria uma tabela de clientes se ela não existir
cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL
    )
""")

# Insere 500 clientes falsos no banco de dados
for _ in range(500):
    nome = fake.first_name()
    ultimo_nome = fake.last_name()
    # Obtenha o primeiro nome do titular
    primeiro_nome = nome.split()[0].lower()
    # Gere um número aleatório de 100 a 999
    numero_aleatorio = random.randint(100, 999)
    # Crie o e-mail com o primeiro nome e o número aleatório
    email = f"{primeiro_nome}{numero_aleatorio}@gmail.com"
    telefone = fake.numerify("(##) 9####-####")
    cursor.execute("INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)", (nome, email, telefone))

# Comita as mudanças e fecha a conexão com o banco de dados
conn.commit()
conn.close()