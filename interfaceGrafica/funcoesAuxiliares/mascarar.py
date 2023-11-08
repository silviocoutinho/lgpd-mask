from utils.imports import mascararPdf
import os.path
from utils.tratamentoErros import mostrarSelecaoCampo, mostrarArquivoInexistente, mostrarErroAoProcessar, mostrarSucessoAoProcessar

def mascarar(app, caminhoArquivo, destino, cpfAtivo, rgAtivo):
    
    entradaCpf = app.children['!entry']
    entradaRg = app.children['!entry2']

    cpf, rg = entradaCpf.get(), entradaRg.get()

    if not (cpfAtivo or rgAtivo):
        mostrarSelecaoCampo("CPF ou RG")
        return  

    if not os.path.isfile(caminhoArquivo):
        mostrarArquivoInexistente()
        return

    try:
        resultado = mascararPdf.mascarar(caminhoArquivo, destino, cpfAtivo, rgAtivo, cpf, rg, entradaCpf, entradaRg)

        if resultado:
            mostrarSucessoAoProcessar(resultado)
    except Exception as e:
        mostrarErroAoProcessar(e)