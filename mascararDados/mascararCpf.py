import re

def removerCpf(pagina, cpfLimpo):
    padraoCpf = re.compile(r'CPF\s*n[°ºº.]*\s*([\d]{3}[-.\s]?[\d]{3}[-.\s]?[\d]{3}[-.\s]?\s?[\d]{2})')
    cpfEncontrados = padraoCpf.findall(pagina.get_text())

    for encontrado in cpfEncontrados:
        cpfPdf = re.sub(r'\D', '', encontrado)
        if cpfPdf == cpfLimpo:
            retangulos = pagina.search_for(encontrado)
            for retangulo in retangulos:
                anotacao = pagina.add_redact_annot(retangulo, fill=(0, 0, 0))
                anotacao.update()
                pagina.apply_redactions()
            return True

    return False
