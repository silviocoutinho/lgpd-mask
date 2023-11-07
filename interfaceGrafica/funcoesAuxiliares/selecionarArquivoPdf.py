import tkinter as tk
from tkinter import filedialog
from utils.tratamentoErros import mostrarErro, mostrarAviso

def selecionarArquivoPdf(app):
    try:
        app.caminhoArquivoPdf = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if app.caminhoArquivoPdf:
            if not app.caminhoArquivoPdf.lower().endswith(".pdf"):
                mostrarAviso("Por favor, selecione um arquivo PDF válido.")
            else:        
                entradaArquivoPdf = app.children['!entry3']
                entradaArquivoPdf.delete(0, tk.END)
                entradaArquivoPdf.insert(0, app.caminhoArquivoPdf)
        else:
            mostrarAviso("Nenhum arquivo selecionado.")
    except Exception as e:
        mostrarErro(f"Ocorreu um erro durante a seleção do arquivo: {e}")
