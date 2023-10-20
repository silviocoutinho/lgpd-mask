import re

def removerCpf(pagina, cpfLimpo):
# Define um padrão de regex para encontrar CPF no texto da página    
    padraoCpf = re.compile(r'CPF\s*n[°ºº.]*\s*([\d]{3}[-.\s]?[\d]{3}[-.\s]?[\d]{3}[-.\s]?\s?[\d]{2})')

# Procura por todas as ocorrências do padrão no texto da página
    cpfEncontrados = padraoCpf.findall(pagina.get_text())

    for encontrado in cpfEncontrados:

# Remove caracteres não numéricos do CPF encontrado        
        cpfPdf = re.sub(r'\D', '', encontrado)

        if cpfPdf == cpfLimpo:

            retangulos = pagina.search_for(encontrado)

            for retangulo in retangulos:
                anotacao = pagina.add_redact_annot(retangulo, fill=(0, 0, 0))
                anotacao.update()
                pagina.apply_redactions()
            return True 

    return False    