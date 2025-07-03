import tkinter as tk
import sqlite3
import os

# Verificar se o arquivo do banco de dados existe e removê-lo se existir
if os.path.exists('clientes.db'):
    os.remove('clientes.db')

# Função para salvar os dados do cliente no banco de dados
def salvar_clientes():
    nome = nome_entry.get()
    telefone = telefone_entry.get()
    endereco = endereco_entry.get() 
    cpf = cpf_entry.get()  
    produto_favorito = produto_favorito_entry.get() 

    # Criar a conexão com o banco
    conn = sqlite3.connect('clientes.db')
    # Criar um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Criar uma tabela no banco de dados caso ela não exista
    cursor.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nome TEXT, telefone TEXT, endereco TEXT, cpf TEXT, produto_favorito TEXT)")
    cursor.execute("INSERT INTO clientes (nome, telefone, endereco, cpf, produto_favorito) VALUES (?, ?, ?, ?, ?)", (nome, telefone, endereco, cpf, produto_favorito))
    conn.commit()
    conn.close()

    # Limpar os campos de entrada para salvar novos dados
    nome_entry.delete(0, tk.END)
    telefone_entry.delete(0, tk.END)
    endereco_entry.delete(0, tk.END)
    cpf_entry.delete(0, tk.END)
    produto_favorito_entry.delete(0, tk.END)

    listar_clientes()

def listar_clientes():
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, nome, telefone, endereco, cpf, produto_favorito FROM clientes')
    clientes = cursor.fetchall()
    conn.close()

    lista_alunos.delete(0, tk.END)

    for cliente in clientes:
        cliente_id, cliente_nome, cliente_telefone, cliente_endereco, cliente_cpf, cliente_produto_favorito = cliente
        lista_alunos.insert(tk.END, f'id: {cliente_id}, Nome: {cliente_nome}, Telefone: {cliente_telefone}, Endereço: {cliente_endereco} CPF: {cliente_cpf} Produto Favorito: {cliente_produto_favorito}')

root = tk.Tk()
root.title("Cadastro de Clientes")
root.minsize(300, 500)

# Criação dos widgets: nome, telefone, endereço, cpf, produto favorito
nome_label = tk.Label(root, text="Nome: ")
nome_entry = tk.Entry(root)

telefone_label = tk.Label(root, text="Telefone: ")
telefone_entry = tk.Entry(root)

endereco_label = tk.Label(root, text="Endereço: ")
endereco_entry = tk.Entry(root)

cpf_label = tk.Label(root, text="CPF: ")
cpf_entry = tk.Entry(root)

produto_favorito_label = tk.Label(root, text="Produto Favorito: ")
produto_favorito_entry = tk.Entry(root)

salvar_button = tk.Button(root, text="Salvar", command=salvar_clientes)
listar_button = tk.Button(root, text="Listar Clientes", command=listar_clientes)

lista_alunos = tk.Listbox(root,width=100)

# Posicionamento dos widgets na janela
nome_label.grid(row=0, column=0, pady=2)
nome_entry.grid(row=0, column=1, pady=2)

telefone_label.grid(row=1, column=0, pady=2)
telefone_entry.grid(row=1, column=1, pady=2)

endereco_label.grid(row=2, column=0, pady=2)
endereco_entry.grid(row=2, column=1, pady=2)

cpf_label.grid(row=3, column=0, pady=2)
cpf_entry.grid(row=3, column=1, pady=2)

produto_favorito_label.grid(row=4, column=0, pady=2)
produto_favorito_entry.grid(row=4, column=1, pady=2)

salvar_button.grid(row=5, column=0, columnspan=2, pady=2)
listar_button.grid(row=6, column=0, columnspan=2, pady=2)

lista_alunos.grid(row=7, column=0, columnspan=2)

root.mainloop()