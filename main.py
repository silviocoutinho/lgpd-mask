import tkinter as tk
from tkinter import filedialog, messagebox
import fitz
import os.path
import re

# Variáveis globais para armazenar o caminho do arquivo PDF e a pasta de destino
caminhoArquivo = ""
destino = ""

# Variáveis globais para controlar se CPF e RG estão ativos
cpfAtivo = True
rgAtivo = True

# Função para ativar o campo CPF
def ativarCPF():
    global cpfAtivo
    cpfAtivo = not cpfAtivo
    entradaCPF.config(state=tk.NORMAL if cpfAtivo else tk.DISABLED)

# Função para ativar o campo RG
def ativarRG():
    global rgAtivo
    rgAtivo = not rgAtivo
    entradaRG.config(state=tk.NORMAL if rgAtivo else tk.DISABLED)

# Função para limpar os campos de entrada
def limparCampos():
    entradaCPF.delete(0, tk.END)
    entradaRG.delete(0, tk.END)
    entradaArquivoPDF.delete(0, tk.END)
    entradaPastaDestino.delete(0, tk.END)

# Função principal para mascarar dados
def mascarar():
    global cpfAtivo, rgAtivo
    cpf = entradaCPF.get()
    rg = entradaRG.get()

    # Verificações iniciais
    if not cpfAtivo and not rgAtivo:
        messagebox.showerror("Erro", "Por favor, selecione pelo menos CPF ou RG.")
        return  # Não continue se ambos estiverem desativados
    elif not os.path.isfile(caminhoArquivo):
        messagebox.showerror("Erro", "O arquivo selecionado não existe.")
        return  # Não continue se o arquivo não existir

    arquivo = caminhoArquivo
    doc = fitz.open(arquivo)
    achouCPF = False
    achouRG = False
    mensagem = []

    # Remove caracteres não numéricos do CPF e RG fornecidos
    cpfLimpo = re.sub(r'\D', '', cpf)
    rgLimpo = re.sub(r'\D', '', rg)

    # Processa CPF
    if cpfAtivo and cpf:
        padraoCPF = re.compile(r'CPF\s*n[°ºº.]*\s*([\d]{3}[-.\s]?[\d]{3}[-.\s]?[\d]{3}[-.\s]?\s?[\d]{2})')
        for pagina in doc:
            texto = pagina.get_text()
            cpfEncontrados = padraoCPF.findall(texto)

            for encontrado in cpfEncontrados:
                cpfPDF = re.sub(r'\D', '', encontrado)
                if cpfPDF == cpfLimpo:
                    retangulos = pagina.search_for(encontrado)
                    for retangulo in retangulos:
                        anotacao = pagina.add_redact_annot(retangulo, fill=(0, 0, 0))
                        anotacao.update()
                        pagina.apply_redactions()
                    achouCPF = True
                    mensagem.append("CPF removido com sucesso.")
                    entradaCPF.delete(0, tk.END)

    # Processa RG
    if rgAtivo and rg:
        padraoRG = re.compile(r'RG\s*n[°ºº.]*\s*((?:[A-Z]+\s*)?[-.\s]?\s*[\d.-]+(?:\s*[–-]\s*[A-Z/]+[A-Z/]+)?)')
        for pagina in doc:
            texto = pagina.get_text()
            rgEncontrados = padraoRG.findall(texto)

            for encontrado in rgEncontrados:
                rgPDF = re.sub(r'\D', '', encontrado)
                if rgPDF == rgLimpo:
                    retangulos = pagina.search_for(encontrado)
                    for retangulo in retangulos:
                        anotacao = pagina.add_redact_annot(retangulo, fill=(0, 0, 0))
                        anotacao.update()
                        pagina.apply_redactions()
                    achouRG = True
                    mensagem.append("RG removido com sucesso.")
                    entradaRG.delete(0, tk.END)

    # Exibe mensagens de resultado
    if mensagem:
        mensagemFinal = []
        if achouCPF:
            mensagemFinal.append("CPF removido com sucesso.")
        if achouRG:
            mensagemFinal.append("RG removido com sucesso.")
        
        nomeArquivoDestino = os.path.basename(caminhoArquivo)
        caminhoDestino = os.path.join(destino, nomeArquivoDestino)
        doc.save(caminhoDestino)
        
        messagebox.showinfo("Sucesso", "\n".join(mensagemFinal))
    else:
        messagebox.showinfo("Informação", "Nenhum dado encontrado para remoção.")

# Função para selecionar um arquivo PDF
def selecionarArquivoPDF():
    global caminhoArquivo
    caminhoArquivoPDF = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    entradaArquivoPDF.delete(0, tk.END)
    entradaArquivoPDF.insert(0, caminhoArquivoPDF)
    caminhoArquivo = caminhoArquivoPDF

# Função para selecionar uma pasta de destino
def selecionarPastaDestino():
    global destino
    pastaDestino = filedialog.askdirectory()
    entradaPastaDestino.delete(0, tk.END)
    entradaPastaDestino.insert(0, pastaDestino)
    destino = pastaDestino

# Criação da interface gráfica usando Tkinter
raiz = tk.Tk()
raiz.title("Mascarar LGPD")
raiz.geometry("650x250")  

# Rótulo do título
rotuloTitulo = tk.Label(raiz, text="Mascarar LGPD")
rotuloTitulo.grid(row=0, column=0, columnspan=4, pady=(10, 5))

# Rótulo e campo de entrada para CPF
rotuloCPF = tk.Label(raiz, text="CPF:")
rotuloCPF.grid(row=1, column=0, sticky="w", padx=10, pady=5)
entradaCPF = tk.Entry(raiz, width=40)
entradaCPF.grid(row=1, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

# Checkbox para habilitar/desabilitar CPF
checkboxCPF = tk.Checkbutton(raiz, text="Ativo", command=ativarCPF)
checkboxCPF.grid(row=1, column=3, padx=10, pady=5)
checkboxCPF.select()

# Rótulo e campo de entrada para RG
rotuloRG = tk.Label(raiz, text="RG:")
rotuloRG.grid(row=2, column=0, sticky="w", padx=10, pady=5)
entradaRG = tk.Entry(raiz, width=40)
entradaRG.grid(row=2, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

# Checkbox para habilitar/desabilitar RG
checkboxRG = tk.Checkbutton(raiz, text="Ativo", command=ativarRG)
checkboxRG.grid(row=2, column=3, padx=10, pady=5)
checkboxRG.select()

# Rótulo e campo de entrada para o arquivo PDF
rotuloArquivoPDF = tk.Label(raiz, text="Arquivo PDF:")
rotuloArquivoPDF.grid(row=3, column=0, sticky="w", padx=10, pady=5)
entradaArquivoPDF = tk.Entry(raiz, width=40)
entradaArquivoPDF.grid(row=3, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

# Botão para selecionar um arquivo PDF
botaoArquivoPDF = tk.Button(raiz, text="Selecionar", command=selecionarArquivoPDF)
botaoArquivoPDF.grid(row=3, column=3, pady=5)

# Rótulo e campo de entrada para a pasta de destino
rotuloPastaDestino = tk.Label(raiz, text="Pasta de destino:")
rotuloPastaDestino.grid(row=4, column=0, sticky="w", padx=10, pady=5)
entradaPastaDestino = tk.Entry(raiz, width=40)
entradaPastaDestino.grid(row=4, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

# Botão para selecionar uma pasta de destino
botaoPastaDestino = tk.Button(raiz, text="Selecionar", command=selecionarPastaDestino)
botaoPastaDestino.grid(row=4, column=3, pady=5)

# Botão para mascarar os dados
botaoMascarar = tk.Button(raiz, text="Mascarar", command=mascarar, width=10)
botaoMascarar.grid(row=5, column=2, sticky="e", padx=10, pady=5)

# Botão para limpar os campos de entrada
botaoLimpar = tk.Button(raiz, text="Limpar", command=limparCampos, width=10)
botaoLimpar.grid(row=5, column=3, sticky="e", pady=5)

# Iniciar a interface gráfica
raiz.mainloop()
