import tkinter as tk
import fitz
import os
import re
from .mascararCpf import removerCpf
from .mascararRg import removerRg

# Função principal para mascarar dados
def mascarar(caminhoArquivo, destino, cpfAtivo, rgAtivo, cpf, rg, entradaCpf, entradaRg):

# Abre o arquivo PDF usando a biblioteca PyMuPDF (fitz)
    doc = fitz.open(caminhoArquivo)

# Inicializa variáveis de controle e mensagens    
    achouCpf = False
    achouRg = False
    mensagem = []

 # Limpa os caracteres não numéricos dos valores de CPF e RG
    cpfLimpo = re.sub(r'\D', '', cpf)
    rgLimpo = re.sub(r'\D', '', rg)

# Itera sobre cada página do documento PDF
    for pagina in doc:

# Verifica se a opção de CPF está ativa e tenta remover o CPF da página
        if cpfAtivo and removerCpf(pagina, cpfLimpo):
            achouCpf = True
            mensagem.append("CPF encontrado com sucesso.")   # Exibe mensagens de resultado

# Verifica se a opção de RG está ativa e tenta remover o RG da página
        if rgAtivo and removerRg(pagina, rgLimpo):
            achouRg = True
            mensagem.append("RG encontrado com sucesso.")    # Exibe mensagens de resultado

# Limpa os campos de entrada de CPF e RG, se os dados foram encontrados e removidos
    if achouCpf:
        entradaCpf.delete(0, tk.END)
    else:
        mensagem.append("CPF não foi encontrado.")

    if achouRg:
        entradaRg.delete(0, tk.END)
    else:
        mensagem.append("RG não foi encontrado.")    

# Se pelo menos um dos dados foi encontrado e removido, salva o PDF mascarado no destino
    if achouCpf or achouRg:
        arquivoDestino = os.path.basename(caminhoArquivo)
        caminhoDestino = os.path.join(destino, arquivoDestino)
        doc.save(caminhoDestino)
        return "\n".join(mensagem)
    else:
        return "\n".join(mensagem)
