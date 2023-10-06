import tkinter as tk
import fitz
import os
import re
from .cpf_mascarar import _remover_cpf
from .rg_mascarar import _remover_rg

def mascarar(caminho_arquivo, destino, cpf_ativo, rg_ativo, cpf, rg, entrada_cpf, entrada_rg):
    doc = fitz.open(caminho_arquivo)
    achou_cpf = False
    achou_rg = False
    mensagem = []

    cpf_limpo = re.sub(r'\D', '', cpf)
    rg_limpo = re.sub(r'\D', '', rg)

    for pagina in doc:
        if cpf_ativo and _remover_cpf(pagina, cpf_limpo):
            achou_cpf = True
            mensagem.append("CPF encontrado com sucesso.")

        if rg_ativo and _remover_rg(pagina, rg_limpo):
            achou_rg = True
            mensagem.append("RG encontrado com sucesso.")

    if achou_cpf:
        entrada_cpf.delete(0, tk.END)
    else:
        mensagem.append("CPF não foi encontrado.")

    if achou_rg:
        entrada_rg.delete(0, tk.END)
    else:
        mensagem.append("RG não foi encontrado.")    

    if achou_cpf or achou_rg:
        nome_arquivo_destino = os.path.basename(caminho_arquivo)
        caminho_destino = os.path.join(destino, nome_arquivo_destino)
        doc.save(caminho_destino)
        return "\n".join(mensagem)
    else:
        return "\n".join(mensagem)
