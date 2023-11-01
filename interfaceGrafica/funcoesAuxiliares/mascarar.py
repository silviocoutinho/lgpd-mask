import os.path
from tkinter import messagebox
import mascararDados.mascararPdf as mascararPdf

def mascarar(app, caminhoArquivo, destino, cpfAtivo, rgAtivo):
    
    entradaCpf = app.children['!entry']
    entradaRg = app.children['!entry2']

    cpf, rg = entradaCpf.get(), entradaRg.get()

    if not (cpfAtivo or rgAtivo):
            messagebox.showerror("Erro", "Por favor, selecione pelo menos CPF ou RG.")
            return  

    if not os.path.isfile(caminhoArquivo):
        messagebox.showerror("Erro", "O arquivo selecionado não existe.")
        return

    try:
        resultado = mascararPdf.mascarar(caminhoArquivo, destino, cpfAtivo, rgAtivo, cpf, rg, entradaCpf, entradaRg)
        messagebox.showinfo("Resultado", resultado)
    except Exception as e:
         messagebox.showerror("Erro", f"Ocorreu um erro ao processar o arquivo PDF: {e}")