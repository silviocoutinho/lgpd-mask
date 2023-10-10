import tkinter as tk
from tkinter import filedialog, messagebox
import os.path
import mascararDados.mascararPdf as mascararPdf
from undoRedo import UndoRedoManager


def create_gui(app):

    # Variáveis globais para armazenar o caminho do arquivo PDF e a pasta de destino
    caminhoArquivo = ""
    destino = ""

    # Variáveis globais para controlar se CPF e RG estão ativos
    cpfAtivo = True
    rgAtivo = True

# Função para ativar o campo CPF
    def ativarCpf():
        nonlocal cpfAtivo
        cpfAtivo = not cpfAtivo
        entradaCpf.config(state=tk.NORMAL if cpfAtivo else tk.DISABLED)

# Função para ativar o campo RG
    def ativarRg():
        nonlocal rgAtivo
        rgAtivo = not rgAtivo
        entradaRg.config(state=tk.NORMAL if rgAtivo else tk.DISABLED)

# Função para limpar os campos de entrada
    def limparCampos():
        entradaCpf.delete(0, tk.END)
        entradaRg.delete(0, tk.END)
        entradaArquivoPdf.delete(0, tk.END)
        entradaPastaDestino.delete(0, tk.END)

# Função principal para mascarar dados
    def mascarar():
        nonlocal caminhoArquivo, destino, cpfAtivo, rgAtivo, entradaCpf, entradaRg

        cpf = entradaCpf.get()
        rg = entradaRg.get()

        if not cpfAtivo and not rgAtivo:
            messagebox.showerror("Erro", "Por favor, selecione pelo menos CPF ou RG.")
            return  # Não continue se ambos estiverem desativados

        if not os.path.isfile(caminhoArquivo):
            messagebox.showerror("Erro", "O arquivo selecionado não existe.")
            return  # Não continue se o arquivo não existir

        resultado = mascararPdf.mascarar(caminhoArquivo, destino, cpfAtivo, rgAtivo, cpf, rg, entradaCpf, entradaRg)

        messagebox.showinfo("Resultado", resultado)

# Função para selecionar um arquivo PDF
    def selecionarArquivoPdf():
        nonlocal caminhoArquivo
        caminhoArquivoPdf = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        entradaArquivoPdf.delete(0, tk.END)
        entradaArquivoPdf.insert(0, caminhoArquivoPdf)
        caminhoArquivo = caminhoArquivoPdf

# Função para selecionar uma pasta de destino
    def selecionarPastaDestino():
        nonlocal destino
        pastaDestino = filedialog.askdirectory()
        entradaPastaDestino.delete(0, tk.END)
        entradaPastaDestino.insert(0, pastaDestino)
        destino = pastaDestino

# Rótulo do título
    rotuloTitulo = tk.Label(app, text="Mascarar LGPD")
    rotuloTitulo.grid(row=0, column=0, columnspan=4, pady=(10, 5))

# Rótulo e campo de entrada para CPF
    rotuloCpf = tk.Label(app, text="CPF:")
    rotuloCpf.grid(row=1, column=0, sticky="w", padx=10, pady=5)
    entradaCpf = tk.Entry(app, width=40)
    undoRedoCpf = UndoRedoManager(entradaCpf)
    entradaCpf.grid(row=1, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

# Checkbox para habilitar/desabilitar CPF
    checkboxCpf = tk.Checkbutton(app, text="Ativo", command=ativarCpf)
    checkboxCpf.grid(row=1, column=3, padx=10, pady=5)
    checkboxCpf.select()

# Rótulo e campo de entrada para RG
    rotuloRg = tk.Label(app, text="RG:")
    rotuloRg.grid(row=2, column=0, sticky="w", padx=10, pady=5)
    entradaRg = tk.Entry(app, width=40)
    undoRedoRg = UndoRedoManager(entradaRg)
    entradaRg.grid(row=2, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

# Checkbox para habilitar/desabilitar RG
    checkboxRg = tk.Checkbutton(app, text="Ativo", command=ativarRg)
    checkboxRg.grid(row=2, column=3, padx=10, pady=5)
    checkboxRg.select()

# Rótulo e campo de entrada para o arquivo PDF
    rotuloArquivoPdf = tk.Label(app, text="Arquivo PDF:")
    rotuloArquivoPdf.grid(row=3, column=0, sticky="w", padx=10, pady=5)
    entradaArquivoPdf = tk.Entry(app, width=40)
    entradaArquivoPdf.grid(row=3, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

# Botão para selecionar um arquivo PDF
    botaoArquivoPdf = tk.Button(app, text="Selecionar", command=selecionarArquivoPdf)
    botaoArquivoPdf.grid(row=3, column=3, pady=5)

# Rótulo e campo de entrada para a pasta de destino
    rotuloPastaDestino = tk.Label(app, text="Pasta de destino:")
    rotuloPastaDestino.grid(row=4, column=0, sticky="w", padx=10, pady=5)
    entradaPastaDestino = tk.Entry(app, width=40)
    entradaPastaDestino.grid(row=4, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

# Botão para selecionar uma pasta de destino
    botaoPastaDestino = tk.Button(app, text="Selecionar", command=selecionarPastaDestino)
    botaoPastaDestino.grid(row=4, column=3, pady=5)

# Botão para mascarar os dados
    botaoMascarar = tk.Button(app, text="Mascarar", command=mascarar, width=10)
    botaoMascarar.grid(row=5, column=2, sticky="e", padx=10, pady=5)

# Botão para limpar os campos de entrada
    botaoLimpar = tk.Button(app, text="Limpar", command=limparCampos, width=10)
    botaoLimpar.grid(row=5, column=3, sticky="e", pady=5)

# Iniciar a interface gráfica
    app.mainloop()
