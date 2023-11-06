import tkinter as tk
from tkinter import messagebox

def mostrarErro(mensagem):
    messagebox.showerror("Erro", mensagem)

def mostrarAviso(mensagem):
    messagebox.showwarning("Aviso", mensagem)