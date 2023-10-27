import tkinter as tk

def limparCampos(entradaCpf, entradaRg, entradaArquivoPdf, entradaPastaDestino):
        entradaCpf.delete(0, tk.END)
        entradaRg.delete(0, tk.END)
        entradaArquivoPdf.delete(0, tk.END)
        entradaPastaDestino.delete(0, tk.END)