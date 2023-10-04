import fitz
import re

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
