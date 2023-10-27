import tkinter as tk

def ativarRg(app, entradaRg):
        app.rgAtivo = not app.rgAtivo
        entradaRg.config(state=tk.NORMAL if app.rgAtivo else tk.DISABLED)