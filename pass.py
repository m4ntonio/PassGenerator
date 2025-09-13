import secrets
import string
import tkinter as tk
from tkinter import messagebox

# --- Funções ---
def gerar_senha(tamanho=16, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(secrets.choice(chars) for _ in range(tamanho))

def mostrar_senha():
    try:
        tamanho = int(entry_tamanho.get())
        if tamanho <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido maior que 0")
        return

    tipo = var_tipo.get()
    if tipo == "Letras":
        chars = string.ascii_letters
    elif tipo == "Letras + Números":
        chars = string.ascii_letters + string.digits
    else:
        chars = string.ascii_letters + string.digits + string.punctuation

    senha = gerar_senha(tamanho, chars)
    label_senha.config(text=senha)
    salvar_senha(senha)

def copiar_senha():
    senha = label_senha.cget("text")
    if senha:
        root.clipboard_clear()
        root.clipboard_append(senha)
        messagebox.showinfo("Copiada!", "Senha copiada para a área de transferência!")
    else:
        messagebox.showwarning("Aviso", "Nenhuma senha gerada ainda!")

def salvar_senha(senha):
    with open("senhas_geradas.txt", "a", encoding="utf-8") as f:
        f.write(senha + "\n")

def sair():
    root.destroy()

def sobre():
    info = (
        "Gerador de Senhas v1.2\n\n"
        "Gera senhas seguras com letras, números e símbolos.\n"
        "As senhas geradas são salvas em 'senhas_geradas.txt'.\n\n"
        "2025 😎 m4ntonio"
    )
    messagebox.showinfo("Sobre", info)

# --- Interface ---
root = tk.Tk()
root.title("Gerador de Senhas")
root.geometry("550x400")
root.resizable(False, False)

# Título
titulo = tk.Label(root, text="🔐 Gerador de Senhas Seguras", font=("Arial", 18, "bold"))
titulo.pack(pady=10)

# Frame para tamanho e tipo
frame_opcoes = tk.Frame(root)
frame_opcoes.pack(pady=10)

tk.Label(frame_opcoes, text="Tamanho:", font=("Arial", 12)).pack(side="left", padx=5)
entry_tamanho = tk.Entry(frame_opcoes, width=5, font=("Arial", 12))
entry_tamanho.insert(0, "16")
entry_tamanho.pack(side="left", padx=5)

tk.Label(frame_opcoes, text="Tipo:", font=("Arial", 12)).pack(side="left", padx=5)
var_tipo = tk.StringVar(value="Completa")
opcoes = ["Letras", "Letras + Números", "Completa"]
menu_tipo = tk.OptionMenu(frame_opcoes, var_tipo, *opcoes)
menu_tipo.config(font=("Arial", 12))
menu_tipo.pack(side="left", padx=5)

# Botões principais
btn_gerar = tk.Button(root, text="Gerar Nova Senha", font=("Arial", 12), command=mostrar_senha)
btn_gerar.pack(pady=10)

btn_copiar = tk.Button(root, text="Copiar Senha", font=("Arial", 12), command=copiar_senha)
btn_copiar.pack(pady=5)

btn_sobre = tk.Button(root, text="Sobre", font=("Arial", 12), command=sobre)
btn_sobre.pack(pady=5)

btn_sair = tk.Button(root, text="Sair", font=("Arial", 12), command=sair)
btn_sair.pack(pady=10)

# Label da senha
label_senha = tk.Label(root, text="", font=("Consolas", 14), wraplength=500, justify="center")
label_senha.pack(pady=20)

root.mainloop()
