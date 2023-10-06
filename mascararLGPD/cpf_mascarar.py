import fitz
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
