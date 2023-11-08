# Mensagem de sucesso
def encontrado(campo):
    return f"{campo} encontrado com sucesso."

# Mensagem de não encontrado
def naoEncontrado(campo):
    return f"{campo} não foi encontrado."

# Mensagens de erro durante a seleção da pasta de destino
def erroSelecaoDestino(e):
    return f"Ocorreu um erro durante a seleção da pasta de destino: {e}"

# Mensagens de erro durante a seleção do arquivo
def erroSelecaoArquivo(e):
    return f"Ocorreu um erro durante a seleção do arquivo: {e}"

# Mensagens gerais

def selecioneCampo(campo):
    return f"Por favor, selecione ao menos um {campo}."

def arquivoNaoExiste():
    return "O arquivo selecionado não existe."

def erroAoProcessar(e):
    return f"Ocorreu um erro ao processar o arquivo PDF: {e}"

def sucessoAoProcessar():
    return "O arquivo foi mascarado com sucesso."

def arquivoInvalido():
    return "Por favor, selecione um arquivo PDF válido."

def erroInesperado(e):
    return f"Ocorreu um erro inesperado: {e}"