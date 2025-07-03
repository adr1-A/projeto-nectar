import tkinter as tk
import sqlite3

#Cria a classe Cadastro de Alunos
class CadastroAlunosWindow:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        master.title("Cadastro de Alunos")

        self.label = tk.Label(master, text="Preencha os dados dos alunos abaixo:", font="Arial 10", bg="cyan")
        self.label.pack()

        self.nome_label = tk.Label(master, text="Nome:")
        self.nome_label.pack()
        self.nome_entry = tk.Entry(master)
        self.nome_entry.pack()

        self.curso_label = tk.Label(master, text="Curso:")
        self.curso_label.pack()
        self.curso_entry = tk.Entry(master)
        self.curso_entry.pack()

        self.ano_matricula_label = tk.Label(master, text="Ano de matrícula:")
        self.ano_matricula_label.pack()
        self.ano_matricula_entry = tk.Entry(master)
        self.ano_matricula_entry.pack()

        self.contato_label = tk.Label(master, text="Informações de contato:")
        self.contato_label.pack()
        self.contato_entry = tk.Entry(master)
        self.contato_entry.pack()

        self.espaco = tk.Label(master, text="")
        self.espaco.pack()

        self.salvar_button = tk.Button(master, text="Salvar", command=self.salvar_alunos, bg="cyan")
        self.salvar_button.pack()
        
    #Cria a def para salvar os Alunos
    def salvar_alunos(self):
        nome = self.nome_entry.get()
        curso = self.curso_entry.get()
        ano_matricula = self.ano_matricula_entry.get()
        info_contato = self.contato_entry.get()

        query = "INSERT INTO alunos (nome, curso, ano_matricula, info_contato) VALUES (?, ?, ?, ?)"
        self.app.cursor.execute(query, (nome, curso, ano_matricula, info_contato))
        self.app.conn.commit()
        self.app.listar_alunos()

        # Limpar os campos após salvar
        self.nome_entry.delete(0, tk.END)
        self.curso_entry.delete(0, tk.END)
        self.ano_matricula_entry.delete(0, tk.END)
        self.contato_entry.delete(0, tk.END)

#Cria a classe Cadastro de Professores
class CadastroProfessoresWindow:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        master.title("Cadastro de Professores")

        self.label = tk.Label(master, text="Preencha os dados dos professores abaixo:", font="Arial 10", bg="orange red", fg="white")
        self.label.pack()

        self.nome_label = tk.Label(master, text="Nome:")
        self.nome_label.pack()
        self.nome_entry = tk.Entry(master)
        self.nome_entry.pack()

        self.matricula_label = tk.Label(master, text="Matrícula:")
        self.matricula_label.pack()
        self.matricula_entry = tk.Entry(master)
        self.matricula_entry.pack()

        self.ano_label = tk.Label(master, text="Disciplinas Lecionadas:")
        self.ano_label.pack()
        self.ano_entry = tk.Entry(master)
        self.ano_entry.pack()

        self.contato_label = tk.Label(master, text="Informações de contato:")
        self.contato_label.pack()
        self.contato_entry = tk.Entry(master)
        self.contato_entry.pack()

        self.espaco = tk.Label(master, text="")
        self.espaco.pack()

        self.salvar_button = tk.Button(master, text="Salvar", command=self.salvar_professor, bg="orange red", fg="white")
        self.salvar_button.pack()

    #Cria a def para salvar os Professores
    def salvar_professor(self):
        nome = self.nome_entry.get()
        matricula = self.matricula_entry.get()
        disciplina = self.ano_entry.get()
        info_contato = self.contato_entry.get()

        query = "INSERT INTO professores (nome, disciplina, matricula, info_contato) VALUES (?, ?, ?, ?)"
        self.app.cursor.execute(query, (nome, disciplina, matricula, info_contato))
        self.app.conn.commit()
        self.app.listar_professores()

        # Limpar os campos após salvar
        self.nome_entry.delete(0, tk.END)
        self.matricula_entry.delete(0, tk.END)
        self.ano_entry.delete(0, tk.END)
        self.contato_entry.delete(0, tk.END)

#Cria a classe Cadastro de Disciplinas
class CadastroDisciplinasWindow:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        master.title("Cadastro de Disciplinas")

        self.label = tk.Label(master, text="Preencha os dados das disciplinas abaixo:", font="Arial 10", bg="light goldenrod")
        self.label.pack()

        self.nome_label = tk.Label(master, text="Nome:")
        self.nome_label.pack()
        self.nome_entry = tk.Entry(master)
        self.nome_entry.pack()

        self.cod_disciplina_label = tk.Label(master, text="Código da Disciplina:")
        self.cod_disciplina_label.pack()
        self.cod_disciplina_entry = tk.Entry(master)
        self.cod_disciplina_entry.pack()

        self.prof_resp_label = tk.Label(master, text="Professor Responsável:")
        self.prof_resp_label.pack()
        self.prof_resp_entry = tk.Entry(master)
        self.prof_resp_entry.pack()

        self.horario_label = tk.Label(master, text="Horário:")
        self.horario_label.pack()
        self.horario_entry = tk.Entry(master)
        self.horario_entry.pack()

        self.sala_label = tk.Label(master, text="Sala:")
        self.sala_label.pack()
        self.sala_entry = tk.Entry(master)
        self.sala_entry.pack()

        self.espaco = tk.Label(master, text="")
        self.espaco.pack()

        self.salvar_button = tk.Button(master, text="Salvar", command=self.salvar_disciplinas, bg="light goldenrod")
        self.salvar_button.pack()

    #Cria a def para salvar as Disciplinas
    def salvar_disciplinas(self):
        nome = self.nome_entry.get()
        codigo = self.cod_disciplina_entry.get()
        professor_responsavel = self.prof_resp_entry.get()
        horario = self.horario_entry.get()
        sala = self.sala_entry.get()

        query = "INSERT INTO disciplinas (nome, codigo, professor_responsavel, horario, sala) VALUES (?, ?, ?, ?, ?)"
        self.app.cursor.execute(query, (nome, codigo, professor_responsavel, horario, sala))
        self.app.conn.commit()
        self.app.listar_disciplinas()

        # Limpar os campos após salvar
        self.nome_entry.delete(0, tk.END)
        self.cod_disciplina_entry.delete(0, tk.END)
        self.prof_resp_entry.delete(0, tk.END)
        self.horario_entry.delete(0, tk.END)
        self.sala_entry.delete(0, tk.END)

class SistemaEducacionalApp:
    def __init__(self, master):
        self.master = master
        master.title("Sistema Educacional")

        self.label = tk.Label(master, text="Bem-vindo ao Sistema Educacional !", font="Arial 14 bold")
        self.label.pack()

        self.label = tk.Label(master, text="Escolha algumas dessas opções de Cadastro:", font="Arial 10")
        self.label.pack()

        self.espaco = tk.Label(master, text="")
        self.espaco.pack()

        self.alunos_button = tk.Button(master, text="Cadastro de Alunos", command=self.abrir_cadastro_alunos, bg="cyan")
        self.alunos_button.pack()

        self.espaco_alunos = tk.Label(master, text="")
        self.espaco_alunos.pack()

        self.professores_button = tk.Button(master, text="Cadastro de Professores", command=self.abrir_cadastro_professores, bg="orange red", fg="white")
        self.professores_button.pack()

        self.espaco_professores = tk.Label(master, text="")
        self.espaco_professores.pack()

        self.disciplinas_button = tk.Button(master, text="Cadastro de Disciplinas", command=self.abrir_cadastro_disciplinas, bg="light goldenrod")
        self.disciplinas_button.pack()

        self.espaco_disciplinas = tk.Label(master, text="")
        self.espaco_disciplinas.pack()

        # Conecta ao banco de dados SQLite
        self.conn = sqlite3.connect('sistema_educacional.db')
        self.cursor = self.conn.cursor()

        # Cria a tabela de alunos
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (
                            id INTEGER PRIMARY KEY,
                            nome TEXT,
                            curso TEXT,
                            ano_matricula INTEGER,
                            info_contato TEXT)''')

        # Cria a tabela de professores
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS professores (
                            id INTEGER PRIMARY KEY,
                            nome TEXT,
                            matricula TEXT,
                            disciplina TEXT,
                            info_contato TEXT)''')

        # Cria a tabela de disciplinas
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS disciplinas (
                            id INTEGER PRIMARY KEY,
                            nome TEXT,
                            codigo TEXT,
                            professor_responsavel TEXT,
                            horario TEXT,
                            sala TEXT)''')       
        self.conn.commit()

    def abrir_cadastro_alunos(self):
        cadastro_alunos_window = tk.Toplevel(self.master)
        cadastro_alunos = CadastroAlunosWindow(cadastro_alunos_window, self)
        cadastro_alunos.cursor = self.cursor
        cadastro_alunos.conexao = self.conn

    def abrir_cadastro_professores(self):
        cadastro_professores_window = tk.Toplevel(self.master)
        cadastro_professores = CadastroProfessoresWindow(cadastro_professores_window, self)
        cadastro_professores.cursor = self.cursor
        cadastro_professores.conexao = self.conn

    def abrir_cadastro_disciplinas(self):
        cadastro_disciplinas_window = tk.Toplevel(self.master)
        cadastro_disciplinas = CadastroDisciplinasWindow(cadastro_disciplinas_window, self)
        cadastro_disciplinas.cursor = self.cursor
        cadastro_disciplinas.conexao = self.conn

    def listar_alunos(self):
        self.espaco_alunos.config(text="Alunos salvos:\n")
        self.cursor.execute("SELECT * FROM alunos")
        alunos = self.cursor.fetchall()
        for aluno in alunos:
            self.espaco_alunos.config(
                text=self.espaco_alunos.cget("text") + str(aluno) + "\n")

    def listar_professores(self):
        self.espaco_professores.config(text="Professores salvos:\n")
        self.cursor.execute("SELECT * FROM professores")
        professores = self.cursor.fetchall()
        for professor in professores:
            self.espaco_professores.config(
                text=self.espaco_professores.cget("text") + str(professor) + "\n")

    def listar_disciplinas(self):
        self.espaco_disciplinas.config(text="Disciplinas salvas:\n")
        self.cursor.execute("SELECT * FROM disciplinas")
        disciplinas = self.cursor.fetchall()
        for disciplina in disciplinas:
            self.espaco_disciplinas.config(
                text=self.espaco_disciplinas.cget("text") + str(disciplina) + "\n")

root = tk.Tk()
root.geometry("400x400")
app = SistemaEducacionalApp(root)
root.mainloop()