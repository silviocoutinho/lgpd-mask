import tkinter as tk
from tkinter import filedialog, messagebox

def selecionarPastaDestino(app):
    try:
        app.pastaDestino = filedialog.askdirectory()
        if app.pastaDestino:
            entradaPastaDestino = app.children['!entry4']
            entradaPastaDestino.delete(0, tk.END)
            entradaPastaDestino.insert(0, app.pastaDestino)
        else:
            entradaPastaDestino = app.children['!entry4']
            entradaPastaDestino.delete(0, tk.END)
            entradaPastaDestino.insert(0, "")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro durante a seleção da pasta de destino: {e}")
