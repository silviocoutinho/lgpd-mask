import tkinter as tk

def ativarCpf(app, entradaCpf):
        app.cpfAtivo = not app.cpfAtivo
        entradaCpf.config(state=tk.NORMAL if app.cpfAtivo else tk.DISABLED)