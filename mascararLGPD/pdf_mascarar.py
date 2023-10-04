import fitz
import os
import re
from .cpf_mascarar import _remover_cpf
from .rg_mascarar import _remover_rg

def mascarar(caminho_arquivo, destino, cpf_ativo, rg_ativo, cpf, rg):
    doc = fitz.open(caminho_arquivo)
    achou_cpf = False
    achou_rg = False
    mensagem = []

    cpf_limpo = re.sub(r'\D', '', cpf)
    rg_limpo = re.sub(r'\D', '', rg)

    for pagina in doc:
        if cpf_ativo and _remover_cpf(pagina, cpf_limpo):
            achou_cpf = True
            mensagem.append("CPF removido com sucesso.")

        if rg_ativo and _remover_rg(pagina, rg_limpo):
            achou_rg = True
            mensagem.append("RG removido com sucesso.")

    if achou_cpf or achou_rg:
        nome_arquivo_destino = os.path.basename(caminho_arquivo)
        caminho_destino = os.path.join(destino, nome_arquivo_destino)
        doc.save(caminho_destino)
        return "\n".join(mensagem)
    else:
        return None
