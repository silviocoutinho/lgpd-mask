import tkinter as tk
from tkinter import messagebox
import os.path
import mascararDados.mascararPdf as mascararPdf
import gui

caminhoArquivo = ""
destino = ""
cpfAtivo = True
rgAtivo = True

def ativarCpf():
    global cpfAtivo
    cpfAtivo = not cpfAtivo
    gui.entradaCpf.config(state=tk.NORMAL if cpfAtivo else tk.DISABLED)

def ativarRg():
    global rgAtivo
    rgAtivo = not rgAtivo
    gui.entradaRg.config(state=tk.NORMAL if rgAtivo else tk.DISABLED)

def limparCampos():
    gui.entradaCpf.delete(0, tk.END)
    gui.entradaRg.delete(0, tk.END)
    gui.entradaArquivoPdf.delete(0, tk.END)
    gui.entradaPastaDestino.delete(0, tk.END)

def mascarar():
    global caminhoArquivo, destino, cpfAtivo, rgAtivo

    cpf = gui.entradaCpf.get()
    rg = gui.entradaRg.get()

    if not cpfAtivo and not rgAtivo:
        messagebox.showerror("Erro", "Por favor, selecione pelo menos CPF ou RG.")
        return

    if not os.path.isfile(caminhoArquivo):
        messagebox.showerror("Erro", "O arquivo selecionado não existe.")
        return  

    resultado = mascararPdf.mascarar(caminhoArquivo, destino, cpfAtivo, rgAtivo, cpf, rg)

    messagebox.showinfo("Resultado", resultado)


if __name__ == "__main__":
    app = tk.Tk()
    app.title("Mascarar LGPD")
    app.geometry("650x250")

    gui.create_gui(app)

    app.mainloop()