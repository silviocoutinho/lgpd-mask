from utils.imports import tk, re, fitz, os
from .mascararCpf import removerCpf
from .mascararRg import removerRg
from utils.tratamentoErros import mostrarErro, mostrarInfo, mostrarAviso

def mascarar(caminhoArquivo, destino, cpfAtivo, rgAtivo, cpf, rg, entradaCpf, entradaRg):

    try:
        doc = fitz.open(caminhoArquivo)

        achouCpf = False
        achouRg = False
        mensagem = []

    # Limpa os caracteres não numéricos dos valores de CPF e RG
        cpfLimpo = re.sub(r'\D', '', cpf)
        rgLimpo = re.sub(r'\D', '', rg)

        for pagina in doc:

            if cpfAtivo and removerCpf(pagina, cpfLimpo):
                achouCpf = True
                mostrarInfo("CPF encontrado com sucesso.")   

            if rgAtivo and removerRg(pagina, rgLimpo):
                achouRg = True
                mostrarInfo("RG encontrado com sucesso.")    

        if achouCpf:
            entradaCpf.delete(0, tk.END)
        else:
            mostrarAviso("CPF não foi encontrado.")

        if achouRg:
            entradaRg.delete(0, tk.END)
        else:
            mostrarAviso("RG não foi encontrado.")    

        if achouCpf or achouRg:
            arquivoDestino = os.path.basename(caminhoArquivo)
            caminhoDestino = os.path.join(destino, arquivoDestino)
            doc.save(caminhoDestino)
            return "\n".join(mensagem)
        else:
            return "\n".join(mensagem)
    
    except Exception as e:
        mostrarErro(f"Ocorreu um erro inesperado: {e}")
