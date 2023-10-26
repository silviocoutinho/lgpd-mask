import tkinter as tk
from tkinter import filedialog

def selecionarPastaDestino(app):
    app.pastaDestino = filedialog.askdirectory()
    entradaPastaDestino = app.children['!entry4']
    entradaPastaDestino.delete(0, tk.END)
    entradaPastaDestino.insert(0, app.pastaDestino)