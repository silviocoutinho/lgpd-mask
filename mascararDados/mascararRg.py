import re

# Função para remover RG de uma página PDF
def removerRg(pagina, rgLimpo):
# Define um padrão de regex para encontrar RG no texto da página
    padraoRG = re.compile(r'RG\s*n[°ºº.]*\s*((?:[A-Z]+\s*)?[-.\s]?\s*[\d.-]+(?:\s*[–-]\s*[A-Z/]+[A-Z/]+)?)')

# Procura por todas as ocorrências do padrão no texto da página
    rgEncontrados = padraoRG.findall(pagina.get_text())

# Itera sobre os RGs encontrados na página
    for encontrado in rgEncontrados:

# Remove caracteres não numéricos do RG encontrado
        rgPdf = re.sub(r'\D', '', encontrado)

# Verifica se o RG encontrado corresponde ao RG que deve ser removido
        if rgPdf == rgLimpo:
            
 # Encontra os retângulos que correspondem ao RG no documento PDF            
            retangulos = pagina.search_for(encontrado)
            
# Itera sobre os retângulos e adiciona anotações de redação (blackout) sobre o RG            
            for retangulo in retangulos:
                anotacao = pagina.add_redact_annot(retangulo, fill=(0, 0, 0))
                anotacao.update()
                pagina.apply_redactions()
            return True # Retorna True se um RG for encontrado e removido

    return False    # Retorna False se nenhum RG for encontrado e removido
