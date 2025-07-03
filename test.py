import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
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

        # Criar e posicionar as imagens iniciais
        self.create_image_button_with_label(master, "funky_republic.png", 0.75, 0.45, self.open_promocao_window, "PROMOÇÃO!!")
        self.create_image_button_with_label(master, "pods.png", 0.25, 0.44, self.open_pods_window, "Pods")
        self.create_image_button_with_label(master, "headshop.png", 0.25, 0.73, self.open_headshop_window, "Headshop")
        self.create_image_button_with_label(master, "combo_essencia.png", 0.75, 0.74, self.open_combo_essencia_window, "Combo Essência")
        
        # Configuração do banco de dados
        self.conn = sqlite3.connect('nectar.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                                id INTEGER PRIMARY KEY,
                                nome TEXT,
                                email TEXT,
                                telefone TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
                                id INTEGER PRIMARY KEY,
                                categoria TEXT,
                                nome TEXT,
                                sabor TEXT,
                                quantidade INTEGER)''')
        produtos = [
                    ('PODS', 'ELFBAR', 'menta', 50),
                    ('PODS', 'ELFBAR', 'blueberry', 50),
                    ('PODS', 'LIFEPOD', 'mango', 50),
                    ('PODS', 'LIFEPOD', 'maça verde', 50),
                    ('PODS', 'LOST MARY', 'morango', 50),
                    ('PODS', 'LOST MARY', 'menta', 50),
                    ('PODS', 'IGNITE', 'banana', 50),
                    ('PODS', 'IGNITE', 'pêssego', 50),
                    ('COMBO ESSÊNCIA', 'ZOMO', 'corinthians', 50),
                    ('COMBO ESSÊNCIA', 'ZOMO', 'chiclete', 50),
                    ('COMBO ESSÊNCIA', 'ZIGGY', 'cereja', 50),
                    ('COMBO ESSÊNCIA', 'ZIGGY', 'limão', 50),
                    ('COMBO ESSÊNCIA', 'ONIX', 'maracujá', 50),
                    ('COMBO ESSÊNCIA', 'ONIX', 'uva', 50),
                    ('PROMOÇÃO', 'FUNKY LANDS', 'melão', 50),
                    ('PROMOÇÃO', 'FUNKY LANDS', 'café', 50),
                    ('HEADSHOP', 'BEM BOLADO', 'preto', 50),
                    ('HEADSHOP', 'BEM BOLADO', 'azul', 50)]
        
        self.cursor.executemany('''INSERT INTO produtos (categoria, nome, sabor, quantidade) VALUES (?, ?, ?, ?)''', produtos)      
        self.conn.commit()

    # Função para criar um botão de imagem com uma label abaixo
    def create_image_button_with_label(self, master, image_path, relx, rely, command, label_text):
        image = tk.PhotoImage(file=image_path)
        button = tk.Button(master, image=image, command=command)
        button.image = image  # Manter uma referência à imagem
        button.place(relx=relx, rely=rely, anchor="center")
    
        label = tk.Label(master, text=label_text, fg="#FEBD59", bg="#5327B0", font="Deka_Ultra_Light 15")
        label.place(relx=relx, rely=rely + 0.11 , anchor="center")

    def open_promocao_window(self):
        self.create_new_window("PROMOÇÃO!!", [("funky_republic.png", self.open_payment_window, 'PROMOÇÃO', 'FUNKY LANDS')])

    def open_pods_window(self):
        self.create_new_window("Pods", [
            ("elfbar.png", self.open_payment_window, 'PODS', 'ELFBAR'),
            ("lifepod.png", self.open_payment_window, 'PODS', 'LIFEPOD'),
            ("lostmary.png", self.open_payment_window, 'PODS', 'LOST MARY'),
            ("ignite.png", self.open_payment_window, 'PODS', 'IGNITE')
        ])

    def open_headshop_window(self):
        self.create_new_window("Headshop", [
            ("headshop.png", self.open_payment_window, 'HEADSHOP', 'BEM BOLADO')
        ])

    def open_combo_essencia_window(self):
        self.create_new_window("Combo Essência", [
            ("zomo.png", self.open_payment_window, 'COMBO ESSÊNCIA', 'ZOMO'),
            ("ziggy.png", self.open_payment_window, 'COMBO ESSÊNCIA', 'ZIGGY'),
            ("onix.png", self.open_payment_window, 'COMBO ESSÊNCIA', 'ONIX')
        ])

    def create_new_window(self, title, images):
        new_window = tk.Toplevel(self.master)
        new_window.title(title)
        new_window.geometry("800x950")

    # Adicionar imagem de fundo na nova janela
        label_bg = tk.Label(new_window, image=self.bg_image)
        label_bg.place(x=0, y=0, relwidth=1, relheight=1)

        num_columns = 4  # Número de colunas na grade
        num_rows = (len(images) - 1) // num_columns + 1  # Número de linhas necessárias

    # Calcular as posições baseadas na grade
        for idx, (image_path, command, categoria, nome) in enumerate(images):
            row = idx // num_columns
            col = idx % num_columns
            relx = 0.2 + col * 0.2
            rely = 0.3 + row * 0.4

            self.create_image_button_with_label(new_window, image_path, relx, rely, lambda cat=categoria, nom=nome: command(cat, nom), nome)


    def open_payment_window(self, categoria, nome):
        payment_window = tk.Toplevel(self.master)
        payment_window.title("Pagamento")
        payment_window.geometry("400x300")

        label_bg = tk.Label(payment_window, image=self.bg_image)
        label_bg.place(x=0, y=0, relwidth=1, relheight=1)

        label_card_number = tk.Label(payment_window, text="Número do Cartão:", fg="#FEBD59", bg="#5327B0")
        label_card_number.place(x=50, y=50)
        self.card_number_entry = tk.Entry(payment_window)
        self.card_number_entry.place(x=200, y=50)

        label_expiry_date = tk.Label(payment_window, text="Data de Validade:", fg="#FEBD59", bg="#5327B0")
        label_expiry_date.place(x=50, y=100)
        self.expiry_date_entry = tk.Entry(payment_window)
        self.expiry_date_entry.place(x=200, y=100)

        label_cvv = tk.Label(payment_window, text="CVV:", fg="#FEBD59", bg="#5327B0")
        label_cvv.place(x=50, y=150)
        self.cvv_entry = tk.Entry(payment_window)
        self.cvv_entry.place(x=200, y=150)

        # Combobox para selecionar o sabor
        label_sabor = tk.Label(payment_window, text="Sabor:", fg="#FEBD59", bg="#5327B0")
        label_sabor.place(x=50, y=200)
        
        sabores = self.get_sabores(categoria, nome)
        self.sabor_combobox = ttk.Combobox(payment_window, values=sabores)
        self.sabor_combobox.place(x=200, y=200)

        pay_button = tk.Button(payment_window, text="Pagar", command=lambda: self.process_payment(categoria, nome, payment_window), bg="#FEBD59", fg="#5327B0")
        pay_button.place(x=150, y=250)

    def get_sabores(self, categoria, nome):
        conn = sqlite3.connect('nectar.db')
        cursor = conn.cursor()
        cursor.execute("SELECT sabor FROM produtos WHERE categoria = ? AND nome = ?", (categoria, nome))
        sabores = [row[0] for row in cursor.fetchall()]
        conn.close()
        return sabores

    def process_payment(self, categoria, nome, window):
        sabor = self.sabor_combobox.get()

        # Aqui você pode adicionar a lógica de processamento de pagamento
        # Como validação dos dados do cartão, comunicação com API de pagamento, etc.
        messagebox.showinfo("Pagamento", "Pagamento Realizado! Agradecemos a preferência")

        # Atualizar quantidade de produto no banco de dados
        self.update_product_quantity(categoria, nome, sabor)

        window.destroy()
        self.master.quit()

    def update_product_quantity(self, categoria, nome, sabor):
        conn = sqlite3.connect('nectar.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE produtos SET quantidade = quantidade - 1 WHERE categoria = ? AND nome = ? AND sabor = ?", (categoria, nome, sabor))
        conn.commit()
        conn.close()

    def open_cadastro_window(self):
        cadastro_window = tk.Toplevel(self.master)
        cadastro_window.title("Cadastro de Cliente")
        cadastro_window.geometry("400x300")
        
        label_bg = tk.Label(cadastro_window, image=self.bg_image)
        label_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Campos do formulário de cadastro
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