import fitz
import os
import re

def _remover_cpf(pagina, cpf_limpo):
    padrao_cpf = re.compile(r'CPF\s*n[°ºº.]*\s*([\d]{3}[-.\s]?[\d]{3}[-.\s]?[\d]{3}[-.\s]?\s?[\d]{2})')
    cpf_encontrados = padrao_cpf.findall(pagina.get_text())

    for encontrado in cpf_encontrados:
        cpf_pdf = re.sub(r'\D', '', encontrado)
        if cpf_pdf == cpf_limpo:
            retangulos = pagina.search_for(encontrado)
            for retangulo in retangulos:
                anotacao = pagina.add_redact_annot(retangulo, fill=(0, 0, 0))
                anotacao.update()
                pagina.apply_redactions()
            return True

    return False

def _remover_rg(pagina, rg_limpo):
    padrao_rg = re.compile(r'RG\s*n[°ºº.]*\s*((?:[A-Z]+\s*)?[-.\s]?\s*[\d.-]+(?:\s*[–-]\s*[A-Z/]+[A-Z/]+)?)')
    rg_encontrados = padrao_rg.findall(pagina.get_text())

    for encontrado in rg_encontrados:
        rg_pdf = re.sub(r'\D', '', encontrado)
        if rg_pdf == rg_limpo:
            retangulos = pagina.search_for(encontrado)
            for retangulo in retangulos:
                anotacao = pagina.add_redact_annot(retangulo, fill=(0, 0, 0))
                anotacao.update()
                pagina.apply_redactions()
            return True

    return False

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
