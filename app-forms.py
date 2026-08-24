import sqlite3
import tkinter as tk
from tkinter import messagebox


# 1. Configuração e Inicialização do Banco de Dados (SQLite)
def inicializar_banco():
    conexao = sqlite3.connect("cadastro_clientes.db")
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


# 2. Funções do Aplicativo
def salvar_cliente():
    nome = entry_nome.get().strip()
    email = entry_email.get().strip()
    telefone = entry_telefone.get().strip()

    # Validação: Garante que todos os campos estejam preenchidos
    if not nome or not email or not telefone:
        messagebox.showwarning(
            "Aviso", "Todos os campos do formulário devem ser preenchidos!"
        )
        return

    try:
        conexao = sqlite3.connect("cadastro_clientes.db")
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
            "Erro", f"Não foi possível salvar no banco de dados.\nErro: {e}"
        )


def limpar_formulario():
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_nome.focus()  # Define o foco inicial de volta para o campo nome


# 3. Construção da Interface Gráfica (Tkinter)
inicializar_banco()

root = tk.Tk()
root.title("Cadastro de Clientes")
root.geometry("400x250")
root.resizable(False, False)

# Labels e Campos de Entrada (Entries)
lbl_nome = tk.Label(root, text="Nome:", font=("Arial", 10))
lbl_nome.grid(row=0, column=0, padx=15, pady=10, sticky="w")
entry_nome = tk.Entry(root, width=35, font=("Arial", 10))
entry_nome.grid(row=0, column=1, padx=15, pady=10)

lbl_email = tk.Label(root, text="E-mail:", font=("Arial", 10))
lbl_email.grid(row=1, column=0, padx=15, pady=10, sticky="w")
entry_email = tk.Entry(root, width=35, font=("Arial", 10))
entry_email.grid(row=1, column=1, padx=15, pady=10)

lbl_telefone = tk.Label(root, text="Telefone:", font=("Arial", 10))
lbl_telefone.grid(row=2, column=0, padx=15, pady=10, sticky="w")
entry_telefone = tk.Entry(root, width=35, font=("Arial", 10))
entry_telefone.grid(row=2, column=1, padx=15, pady=10)

# Container para os botões alinhados lado a lado
frame_botoes = tk.Frame(root)
frame_botoes.grid(row=3, column=0, columnspan=2, pady=20)

btn_salvar = tk.Button(
    frame_botoes,
    text="Salvar Cliente",
    command=salvar_cliente,
    bg="#4CAF50",
    fg="white",
    width=13,
    font=("Arial", 10, "bold"),
)
btn_salvar.pack(side=tk.LEFT, padx=10)

btn_limpar = tk.Button(
    frame_botoes,
    text="Limpar",
    command=limpar_formulario,
    bg="#f44336",
    fg="white",
    width=13,
    font=("Arial", 10, "bold"),
)
btn_limpar.pack(side=tk.LEFT, padx=10)

# Inicia o loop da interface gráfica
root.mainloop()
