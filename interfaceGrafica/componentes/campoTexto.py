import tkinter as tk

def criarCampoTexto(app, width, row, column):
    campoTexto = tk.Entry(app, width=width)
    campoTexto.grid(row=row, column=column, sticky='ew')
    return campoTexto