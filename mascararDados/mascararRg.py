import re

def removerRg(pagina, rgLimpo):
# Define um padrão de regex para encontrar RG no texto da página
    padraoRG = re.compile(r'RG\s*n[°ºº.]*\s*((?:[A-Z]+\s*)?[-.\s]?\s*[\d.-]+(?:\s*[–-]\s*[A-Z/]+[A-Z/]+)?)')

# Procura por todas as ocorrências do padrão no texto da página
    rgEncontrados = padraoRG.findall(pagina.get_text())

    for encontrado in rgEncontrados:

# Remove caracteres não numéricos do RG encontrado
        rgPdf = re.sub(r'\D', '', encontrado)

        if rgPdf == rgLimpo:
            
            retangulos = pagina.search_for(encontrado)
            
            for retangulo in retangulos:
                anotacao = pagina.add_redact_annot(retangulo, fill=(0, 0, 0))
                anotacao.update()
                pagina.apply_redactions()
            return True 

    return False    