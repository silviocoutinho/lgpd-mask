import os.path
from tkinter import messagebox
import mascararDados.mascararPdf as mascararPdf

def mascarar(app, caminhoArquivo, destino, cpfAtivo, rgAtivo):
    
    entradaCpf = app.children['!entry']
    entradaRg = app.children['!entry2']

    cpf = entradaCpf.get()
    rg = entradaRg.get()

    if not cpfAtivo and not rgAtivo:
            messagebox.showerror("Erro", "Por favor, selecione pelo menos CPF ou RG.")
            return  

    if not os.path.isfile(caminhoArquivo):
        messagebox.showerror("Erro", "O arquivo selecionado não existe.")
        return

    resultado = mascararPdf.mascarar(caminhoArquivo, destino, cpfAtivo, rgAtivo, cpf, rg, entradaCpf, entradaRg)
    messagebox.showinfo("Resultado", resultado)