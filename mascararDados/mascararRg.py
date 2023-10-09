import re

def removerRg(pagina, rgLimpo):
    padraoRG = re.compile(r'RG\s*n[°ºº.]*\s*((?:[A-Z]+\s*)?[-.\s]?\s*[\d.-]+(?:\s*[–-]\s*[A-Z/]+[A-Z/]+)?)')
    rgEncontrados = padraoRG.findall(pagina.get_text())

    for encontrado in rgEncontrados:
        rgPdf = re.sub(r'\D', '', encontrado)
        if rgPdf == rgLimpo:
            retangulos = pagina.search_for(encontrado)
            for retangulo in retangulos:
                anotacao = pagina.add_redact_annot(retangulo, fill=(0, 0, 0))
                anotacao.update()
                pagina.apply_redactions()
            return True

    return False
