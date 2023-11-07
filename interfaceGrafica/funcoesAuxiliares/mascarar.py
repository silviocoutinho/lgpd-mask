import os.path
from tkinter import messagebox
import mascararDados.mascararPdf as mascararPdf
from utils.tratamentoErros import mostrarErro, mostrarAviso, mostrarInfo

def mascarar(app, caminhoArquivo, destino, cpfAtivo, rgAtivo):
    
    entradaCpf = app.children['!entry']
    entradaRg = app.children['!entry2']

    cpf, rg = entradaCpf.get(), entradaRg.get()

    if not (cpfAtivo or rgAtivo):
        mostrarAviso("Por favor, selecione pelo menos CPF ou RG.")
        return  

    if not os.path.isfile(caminhoArquivo):
        mostrarAviso("O arquivo selecionado não existe.")
        return

    try:
        resultado = mascararPdf.mascarar(caminhoArquivo, destino, cpfAtivo, rgAtivo, cpf, rg, entradaCpf, entradaRg)
        if resultado:
            mostrarInfo(resultado)
    except Exception as e:
        mostrarErro(f"Ocorreu um erro ao processar o arquivo PDF: {e}")