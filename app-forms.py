import sqlite3
import tkinter as tk
from tkinter import messagebox


# --- CONFIGURAÇÃO DO BANCO DE DADOS ---
def inicializar_banco():
    """Cria o banco de dados e a tabela se não existirem."""
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL
        )
        """
    )
    conexao.commit()
    conexao.close()


# --- FUNÇÕES INTERNAS DO SISTEMA ---
def salvar_cliente():
    """Valida os campos e salva os dados no banco de dados."""
    nome = entry_nome.get().strip()
    email = entry_email.get().strip()
    telefone = entry_telefone.get().strip()

    # Validação de campos vazios
    if not nome or not email or not telefone:
        messagebox.showwarning(
            "Alerta", "Todos os campos devem ser preenchidos!"
        )
        return

    try:
        conexao = sqlite3.connect("clientes.db")
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)",
            (nome, email, telefone),
        )

        conexao.commit()
        conexao.close()

        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        limpar_formulario()

    except Exception as e:
        messagebox.showerror(
            "Erro", f"Erro ao salvar no banco de dados: {e}"
        )


def limpar_formulario():
    """Limpa todos os campos de entrada de texto."""
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)


# --- NOVA FUNÇÃO: VISUALIZAR CLIENTES ---
def visualizar_clientes():
    """Abre uma nova janela e exibe todos os clientes cadastrados."""

    janela_clientes = tk.Toplevel(janela)
    janela_clientes.title("Clientes Cadastrados")
    janela_clientes.geometry("600x350")
    janela_clientes.resizable(False, False)

    # Título
    lbl_titulo = tk.Label(
        janela_clientes,
        text="Clientes Cadastrados",
        font=("Arial", 14, "bold")
    )
    lbl_titulo.pack(pady=10)

    # Área onde os clientes serão exibidos
    lista_clientes = tk.Text(
        janela_clientes,
        width=70,
        height=15,
        font=("Arial", 10)
    )
    lista_clientes.pack(padx=10, pady=10)

    try:
        conexao = sqlite3.connect("clientes.db")
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT id, nome, email, telefone FROM clientes"
        )

        clientes = cursor.fetchall()

        conexao.close()

        if not clientes:
            lista_clientes.insert(
                tk.END,
                "Nenhum cliente cadastrado."
            )
        else:
            for cliente in clientes:
                id_cliente, nome, email, telefone = cliente

                lista_clientes.insert(
                    tk.END,
                    f"ID: {id_cliente}\n"
                    f"Nome: {nome}\n"
                    f"E-mail: {email}\n"
                    f"Telefone: {telefone}\n"
                    + "-" * 60 + "\n"
                )

        # Impede edição do conteúdo
        lista_clientes.config(state="disabled")

    except Exception as e:
        messagebox.showerror(
            "Erro",
            f"Erro ao consultar o banco de dados: {e}"
        )


# --- INTERFACE GRÁFICA (Tkinter) ---

# Inicializa o banco de dados
inicializar_banco()

# Criação da janela principal
janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("450x300")
janela.resizable(False, False)


# --- CAMPOS DO FORMULÁRIO ---

lbl_nome = tk.Label(
    janela,
    text="Nome:",
    font=("Arial", 10)
)
lbl_nome.grid(
    row=0,
    column=0,
    padx=20,
    pady=10,
    sticky="w"
)

entry_nome = tk.Entry(
    janela,
    width=35
)
entry_nome.grid(
    row=0,
    column=1,
    padx=10,
    pady=10
)


lbl_email = tk.Label(
    janela,
    text="E-mail:",
    font=("Arial", 10)
)
lbl_email.grid(
    row=1,
    column=0,
    padx=20,
    pady=10,
    sticky="w"
)

entry_email = tk.Entry(
    janela,
    width=35
)
entry_email.grid(
    row=1,
    column=1,
    padx=10,
    pady=10
)


lbl_telefone = tk.Label(
    janela,
    text="Telefone:",
    font=("Arial", 10)
)
lbl_telefone.grid(
    row=2,
    column=0,
    padx=20,
    pady=10,
    sticky="w"
)

entry_telefone = tk.Entry(
    janela,
    width=35
)
entry_telefone.grid(
    row=2,
    column=1,
    padx=10,
    pady=10
)


# --- BOTÕES ---

btn_salvar = tk.Button(
    janela,
    text="Salvar",
    command=salvar_cliente,
    bg="#4CAF50",
    fg="white",
    width=12
)
btn_salvar.grid(
    row=3,
    column=0,
    padx=10,
    pady=15
)


btn_limpar = tk.Button(
    janela,
    text="Limpar",
    command=limpar_formulario,
    bg="#f44336",
    fg="white",
    width=12
)
btn_limpar.grid(
    row=3,
    column=1,
    padx=10,
    pady=15
)


# --- NOVO BOTÃO: VISUALIZAR CLIENTES ---

btn_visualizar = tk.Button(
    janela,
    text="Visualizar Clientes",
    command=visualizar_clientes,
    bg="#2196F3",
    fg="white",
    width=25
)
btn_visualizar.grid(
    row=4,
    column=0,
    columnspan=2,
    pady=10
)


# --- EXECUTA O PROGRAMA ---
janela.mainloop()
