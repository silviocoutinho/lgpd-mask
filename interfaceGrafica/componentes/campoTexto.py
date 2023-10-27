import tkinter as tk
from ..funcoesAuxiliares.desfazerRefazer import desfazerRefazer

def criarCampoTexto(app, width, row, column):
    campoTexto = tk.Entry(app, width=width)
    campoTexto.grid(row=row, column=column, sticky='ew')
    campoTexto = desfazerRefazer(campoTexto)
    return campoTexto