import tkinter as tk
from tkinter import messagebox
import os.path
import mascararDados.mascararPdf as mascararPdf
import gui

# Variáveis globais para armazenar o caminho do arquivo PDF e a pasta de destino
caminhoArquivo = ""
destino = ""
cpfAtivo = True
rgAtivo = True

# Função para ativar o campo CPF
def ativarCpf():
    global cpfAtivo
    cpfAtivo = not cpfAtivo
    gui.entradaCpf.config(state=tk.NORMAL if cpfAtivo else tk.DISABLED)

# Função para ativar o campo RG
def ativarRg():
    global rgAtivo
    rgAtivo = not rgAtivo
    gui.entradaRg.config(state=tk.NORMAL if rgAtivo else tk.DISABLED)

# Função para limpar os campos de entrada
def limparCampos():
    gui.entradaCpf.delete(0, tk.END)
    gui.entradaRg.delete(0, tk.END)
    gui.entradaArquivoPdf.delete(0, tk.END)
    gui.entradaPastaDestino.delete(0, tk.END)

# Função principal para mascarar dados
def mascarar():
    global caminhoArquivo, destino, cpfAtivo, rgAtivo

    cpf = gui.entradaCpf.get()
    rg = gui.entradaRg.get()

# Verificações iniciais
    if not cpfAtivo and not rgAtivo:
        messagebox.showerror("Erro", "Por favor, selecione pelo menos CPF ou RG.")
        return  # Não continue se ambos estiverem desativados

    if not os.path.isfile(caminhoArquivo):
        messagebox.showerror("Erro", "O arquivo selecionado não existe.")
        return  # Não continue se o arquivo não existir

    resultado = mascararPdf.mascarar(caminhoArquivo, destino, cpfAtivo, rgAtivo, cpf, rg)

    messagebox.showinfo("Resultado", resultado)


if __name__ == "__main__":
    # Criar a janela principal
    app = tk.Tk()
    app.title("Mascarar LGPD")
    app.geometry("650x250")

    # Chamar a função para criar a interface gráfica a partir de gui.py
    gui.create_gui(app)

    app.mainloop()