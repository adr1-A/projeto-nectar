import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import random
from faker import Faker

fake = Faker('pt_BR')

class NectarApp:
    def __init__(self, master):
        self.master = master
        master.title("NECTAR APP")
        master.geometry("800x950")
        master.resizable(False, False)  # Travar o redimensionamento da janela principal

        # Alterar o estilo da janela
        self.style = ttk.Style()
        self.style.theme_use('clam')  # Escolher um tema para personalizar

        # Alterar a cor do topo da janela (barra de título)
        self.style.configure('TFrame', background='#FEBD59')  # Cor de fundo da janela

        # Widget para exibir a mensagem de cadastro concluído
        self.message_label = tk.Label(master, text="", fg="green", bg="#5327B0", font="Deka_Ultra_Light 15")
        self.message_label.place(relx=0.5, rely=0.9, anchor="center")
        
        # Definir o ícone da janela principal
        master.iconbitmap("icone.ico")  # Substitua "icone.ico" pelo caminho do seu ícone

        self.bg_image = tk.PhotoImage(file="nectar_fundo.png")
        self.label_bg = tk.Label(master, image=self.bg_image)
        self.label_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Adicionar logo da NECTAR
        self.logo_image = tk.PhotoImage(file="logo.png")  # Substitua "logo.png" pelo caminho do seu logo
        self.logo_label = tk.Label(master, image=self.logo_image, bg="#5327B0")
        self.logo_label.place(relx=0.5, rely=0.24, anchor="center")

        # Botão de Cadastro
        self.cadastro_button = tk.Button(master, text="Cadastro", bg="#5327B0", fg="#FEBD59", command=self.open_cadastro_window)
        self.cadastro_button.place(x=2.5, y=2.5)

        # Rótulo do nome do usuário (inicialmente vazio)
        self.user_label = tk.Label(master, text="", fg="#FEBD59", bg="#5327B0", font="Deka_Ultra_Light 15")
        self.user_label.place(x=2.5, y=2.5)

        # Criar e posicionar as imagens com texto usando place
        self.create_image_with_text("Pods", "pods.png", 0.25, 0.44, text_offset=0.13, bg_color="#FEBD59")
        self.create_image_with_text("Headshop", "headshop.png", 0.75, 0.45, text_offset=0.13, bg_color="#FEBD59")
        self.create_image_with_text("PROMOÇÃO !!", "funky_republic.png", 0.25, 0.73, text_offset=0.13, bg_color="#FEBD59")
        self.create_image_with_text("Combo Essência", "combo_essencia.png", 0.75, 0.74, text_offset=0.115, bg_color="#FEBD59")

        self.setup_database()

    def create_image_with_text(self, text, image_path, relx, rely, text_offset, bg_color):
        # Carregar a imagem de fundo usando PhotoImage
        bg_image = tk.PhotoImage(file=image_path)
        
        # Criar um Label com a imagem de fundo e o texto sobre ela
        label_bg = tk.Label(self.master, image=bg_image, bg=bg_color)
        label_bg.image = bg_image  # Manter uma referência para evitar que a imagem seja coletada pelo garbage collector
        label_bg.place(relx=relx, rely=rely, anchor="center")
        label_bg.bind("<Button-1>", lambda e: self.open_new_window(text))
        
        label_text = tk.Label(self.master, text=text, fg="#FEBD59", bg="#5327B0", font="Deka_Ultra_Light 15")
        label_text.place(relx=relx, rely=rely + text_offset, anchor="center")  # Usar text_offset para ajustar a altura do texto

    def open_new_window(self, title):
        new_window = tk.Toplevel(self.master)
        new_window.title(title)
        new_window.geometry("800x950")  # Definir as dimensões da nova janela
        new_window.resizable(False, False)  # Travar o redimensionamento da nova janela

        # Alterar o estilo da nova janela
        style = ttk.Style(new_window)
        style.theme_use('clam')  # Escolher um tema para personalizar

        # Alterar a cor do topo da nova janela (barra de título)
        style.configure('TFrame', background='#FEBD59')  # Cor de fundo da janela

        # Definir o ícone da nova janela
        new_window.iconbitmap("icone.ico")  # Substitua "icone.ico" pelo caminho do seu ícone

        # Adicionar a mesma imagem de fundo na nova janela
        label_bg = tk.Label(new_window, image=self.bg_image)
        label_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Adicionar novas imagens na nova janela
        positions = [(0.25, 0.2), (0.75, 0.2), (0.25, 0.4), (0.75, 0.4), 
                     (0.25, 0.6), (0.75, 0.6), (0.25, 0.8), (0.75, 0.8)]
        images = ["nova_imagem1.png", "nova_imagem2.png", "nova_imagem3.png", "nova_imagem4.png",
                  "nova_imagem5.png", "nova_imagem6.png", "nova_imagem7.png", "nova_imagem8.png"]

        for (relx, rely), img in zip(positions, images):
            self.add_image_to_window(new_window, img, relx, rely)

    def add_image_to_window(self, window, image_path, relx, rely):
        image = tk.PhotoImage(file=image_path)
        
        label_img = tk.Label(window, image=image)
        label_img.image = image  # Manter uma referência para evitar que a imagem seja coletada pelo garbage collector
        label_img.place(relx=relx, rely=rely, anchor="center")

    def setup_database(self):
        # Conectar ao banco de dados SQLite (ou criar um novo banco de dados)
        self.conn = sqlite3.connect("nectar_db.sqlite")
        self.cursor = self.conn.cursor()

        # Criar uma tabela de clientes se ela não existir
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL
            )
        """)

        # Criar uma tabela de produtos se ela não existir
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
            )
        """)

        # Criar uma tabela de vendas se ela não existir
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS vendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto_id INTEGER NOT NULL,
            quantidade INTEGER NOT NULL,
            data_venda TEXT NOT NULL,
            FOREIGN KEY (produto_id) REFERENCES produtos (id)
            )
        """)

        self.conn.commit()

    def open_cadastro_window(self):
        cadastro_window = tk.Toplevel(self.master)
        cadastro_window.title("Cadastro de Cliente")
        cadastro_window.geometry("300x300")
        cadastro_window.resizable(False, False)
        
        cadastro_window.configure(bg="#5327B0")

        style = ttk.Style(cadastro_window)
        style.theme_use('clam')

        style.configure('TFrame', background='#FEBD59')

        cadastro_window.iconbitmap("icone.ico")

        # Labels e Entrys para o cadastro, centralizados
        label_nome = tk.Label(cadastro_window, text="Nome:", fg="#FEBD59", bg="#5327B0")
        label_nome.place(x=50, y=50)
        self.nome_entry = tk.Entry(cadastro_window)
        self.nome_entry.place(x=120, y=50)

        label_email = tk.Label(cadastro_window, text="Email:", fg="#FEBD59", bg="#5327B0")
        label_email.place(x=50, y=100)
        self.email_entry = tk.Entry(cadastro_window)
        self.email_entry.place(x=120, y=100)

        label_telefone = tk.Label(cadastro_window, text="Telefone:", fg="#FEBD59", bg="#5327B0")
        label_telefone.place(x=50, y=150)
        self.telefone_entry = tk.Entry(cadastro_window)
        self.telefone_entry.place(x=120, y=150)

        # Botão para salvar o cadastro, centralizado
        save_button = tk.Button(cadastro_window, text="Salvar", command=self.save_cadastro, bg="#FEBD59", fg="#5327B0")
        save_button.place(x=120, y=200)

    def save_cadastro(self):    
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        telefone = self.telefone_entry.get()

        # Inserir os dados do cliente no banco de dados
        self.cursor.execute("INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)", (nome, email, telefone))
        self.conn.commit()

        # Chamar a função para mostrar a mensagem com o nome do cliente cadastrado
        self.show_message(f"Cliente '{nome}' cadastrado com sucesso!")

        # Ocultar o botão "Cadastro"
        self.cadastro_button.place_forget()

        # Exibir o nome do usuário no topo esquerdo
        self.user_label.config(text=nome)

        # Limpar os campos de entrada
        self.nome_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.telefone_entry.delete(0, tk.END)
        
    def show_message(self, message):
        # Atualizar o texto da Label da mensagem
        self.message_label.config(text=message)
        # Exibir a Label da mensagem por 3 segundos
        self.master.after(3000, lambda: self.message_label.config(text=""))
    
        messagebox.showinfo("Cadastro", "Cliente cadastrado com sucesso!")

if __name__ == "__main__":
    root = tk.Tk()
    app = NectarApp(root)
    root.mainloop()