import sqlite3

# Conecta ao banco de dados SQLite
conn = sqlite3.connect("nectar_db.sqlite")
cursor = conn.cursor()

# Executa uma instrução SQL para excluir todos os registros da tabela clientes
cursor.execute("DELETE FROM clientes")

# Redefine o contador de ID da tabela clientes
cursor.execute("DELETE FROM sqlite_sequence WHERE name='clientes'")

# Comita as mudanças e fecha a conexão com o banco de dados
conn.commit()
conn.close()
