import tkinter as tk
from tkinter import messagebox
import os.path
import mascararDados.mascararPdf as mascararPdf
import gui

caminhoArquivo = ""
destino = ""
cpfAtivo = True
rg_ativo = True

def ativar_cpf():
    global cpfAtivo
    cpfAtivo = not cpfAtivo
    gui.entrada_cpf.config(state=tk.NORMAL if cpfAtivo else tk.DISABLED)

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
    global caminhoArquivo, destino, cpfAtivo, rg_ativo

    cpf = gui.entrada_cpf.get()
    rg = gui.entrada_rg.get()

    if not cpfAtivo and not rg_ativo:
        messagebox.showerror("Erro", "Por favor, selecione pelo menos CPF ou RG.")
        return

    if not os.path.isfile(caminhoArquivo):
        messagebox.showerror("Erro", "O arquivo selecionado não existe.")
        return

    resultado = mascararPdf.mascarar(caminhoArquivo, destino, cpfAtivo, rg_ativo, cpf, rg)

    messagebox.showinfo("Resultado", resultado)


if __name__ == "__main__":
    # Criar a janela principal
    app = tk.Tk()
    app.title("Mascarar LGPD")
    app.geometry("650x250")

    # Chamar a função para criar a interface gráfica a partir de gui.py
    gui.create_gui(app)

    app.mainloop()