import tkinter as tk

def limparCampos(*campos):
    for campo in campos:
        if isinstance(campo, tk.Entry):
            campo.delete(0, tk.END)
