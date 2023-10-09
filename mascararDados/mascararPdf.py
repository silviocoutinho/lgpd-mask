import tkinter as tk
import fitz
import os
import re
from .mascararCpf import removerCpf
from .rg_mascarar import _remover_rg

def mascarar(caminhoArquivo, destino, cpfAtivo, rg_ativo, cpf, rg, entradaCpf, entrada_rg):
    doc = fitz.open(caminhoArquivo)
    achouCpf = False
    achou_rg = False
    mensagem = []

    cpfLimpo = re.sub(r'\D', '', cpf)
    rg_limpo = re.sub(r'\D', '', rg)

    for pagina in doc:
        if cpfAtivo and removerCpf(pagina, cpfLimpo):
            achouCpf = True
            mensagem.append("CPF encontrado com sucesso.")

        if rg_ativo and _remover_rg(pagina, rg_limpo):
            achou_rg = True
            mensagem.append("RG encontrado com sucesso.")

    if achouCpf:
        entradaCpf.delete(0, tk.END)
    else:
        mensagem.append("CPF não foi encontrado.")

    if achou_rg:
        entrada_rg.delete(0, tk.END)
    else:
        mensagem.append("RG não foi encontrado.")    

    if achouCpf or achou_rg:
        arquivoDestino = os.path.basename(caminhoArquivo)
        caminhoDestino = os.path.join(destino, arquivoDestino)
        doc.save(caminhoDestino)
        return "\n".join(mensagem)
    else:
        return "\n".join(mensagem)
