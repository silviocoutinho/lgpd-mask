import tkinter as tk
import fitz
import os
import re
from .mascararCpf import removerCpf
from .mascararRg import removerRg

def mascarar(caminhoArquivo, destino, cpfAtivo, rgAtivo, cpf, rg, entradaCpf, entradaRg):

    doc = fitz.open(caminhoArquivo)

    achouCpf = False
    achouRg = False
    mensagem = []

 # Limpa os caracteres não numéricos dos valores de CPF e RG
    cpfLimpo = re.sub(r'\D', '', cpf)
    rgLimpo = re.sub(r'\D', '', rg)

    for pagina in doc:

        if cpfAtivo and removerCpf(pagina, cpfLimpo):
            achouCpf = True
            mensagem.append("CPF encontrado com sucesso.")   

        if rgAtivo and removerRg(pagina, rgLimpo):
            achouRg = True
            mensagem.append("RG encontrado com sucesso.")    

    if achouCpf:
        entradaCpf.delete(0, tk.END)
    else:
        mensagem.append("CPF não foi encontrado.")

    if achouRg:
        entradaRg.delete(0, tk.END)
    else:
        mensagem.append("RG não foi encontrado.")    

    if achouCpf or achouRg:
        arquivoDestino = os.path.basename(caminhoArquivo)
        caminhoDestino = os.path.join(destino, arquivoDestino)
        doc.save(caminhoDestino)
        return "\n".join(mensagem)
    else:
        return "\n".join(mensagem)
