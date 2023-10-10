import re

# Função para remover CPF de uma página PDF
def removerCpf(pagina, cpfLimpo):
# Define um padrão de regex para encontrar CPF no texto da página    
    padraoCpf = re.compile(r'CPF\s*n[°ºº.]*\s*([\d]{3}[-.\s]?[\d]{3}[-.\s]?[\d]{3}[-.\s]?\s?[\d]{2})')

# Procura por todas as ocorrências do padrão no texto da página
    cpfEncontrados = padraoCpf.findall(pagina.get_text())

 # Itera sobre os CPFs encontrados na página
    for encontrado in cpfEncontrados:

# Remove caracteres não numéricos do CPF encontrado        
        cpfPdf = re.sub(r'\D', '', encontrado)

# Verifica se o CPF encontrado corresponde ao CPF que deve ser removido
        if cpfPdf == cpfLimpo:

# Encontra os retângulos que correspondem ao CPF no documento PDF
            retangulos = pagina.search_for(encontrado)

# Itera sobre os retângulos e adiciona anotações de redação (blackout) sobre o CPF
            for retangulo in retangulos:
                anotacao = pagina.add_redact_annot(retangulo, fill=(0, 0, 0))
                anotacao.update()
                pagina.apply_redactions()
            return True # Retorna True se um CPF for encontrado e removido

    return False    # Retorna False se nenhum CPF for encontrado e removido
