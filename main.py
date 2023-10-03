import tkinter as tk
from tkinter import filedialog, messagebox
import os.path
import mascararLGPD.pdf_mascarar as pdf_mascarar
import gui

caminho_arquivo = ""
destino = ""
cpf_ativo = True
rg_ativo = True

def ativar_cpf():
    global cpf_ativo
    cpf_ativo = not cpf_ativo
    gui.entrada_cpf.config(state=tk.NORMAL if cpf_ativo else tk.DISABLED)

def ativar_rg():
    global rg_ativo
    rg_ativo = not rg_ativo
    gui.entrada_rg.config(state=tk.NORMAL if rg_ativo else tk.DISABLED)

def limpar_campos():
    gui.entrada_cpf.delete(0, tk.END)
    gui.entrada_rg.delete(0, tk.END)
    gui.entrada_arquivo_pdf.delete(0, tk.END)
    gui.entrada_pasta_destino.delete(0, tk.END)

def mascarar():
    global caminho_arquivo, destino, cpf_ativo, rg_ativo

    cpf = gui.entrada_cpf.get()
    rg = gui.entrada_rg.get()

    if not cpf_ativo and not rg_ativo:
        messagebox.showerror("Erro", "Por favor, selecione pelo menos CPF ou RG.")
        return

    if not os.path.isfile(caminho_arquivo):
        messagebox.showerror("Erro", "O arquivo selecionado não existe.")
        return

    resultado = pdf_mascarar.mascarar(caminho_arquivo, destino, cpf_ativo, rg_ativo, cpf, rg)

    if resultado:
        messagebox.showinfo("Sucesso", resultado)
    else:
        messagebox.showinfo("Informação", "Nenhum dado encontrado para remoção.")

if __name__ == "__main__":
    app = gui.create_app()
    app.mainloop()
