import tkinter as tk
from tkinter import filedialog

def selecionarArquivoPdf(app):

    app.caminhoArquivoPdf = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    entradaArquivoPdf = app.children['!entry3']
    entradaArquivoPdf.delete(0, tk.END)
    entradaArquivoPdf.insert(0, app.caminhoArquivoPdf)