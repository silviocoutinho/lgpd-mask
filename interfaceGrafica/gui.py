import tkinter as tk
from tkinter import filedialog
from .desfazerRefazer import desfazerRefazer
from interfaceGrafica.mascarar import mascarar

def create_gui(app):

    app.caminhoArquivoPdf = ""
    app.pastaDestino = ""

    app.cpfAtivo = True
    app.rgAtivo = True

    def ativarCpf():
        app.cpfAtivo = not app.cpfAtivo
        entradaCpf.config(state=tk.NORMAL if app.cpfAtivo else tk.DISABLED)

    def ativarRg():
        app.rgAtivo = not app.rgAtivo
        entradaRg.config(state=tk.NORMAL if app.rgAtivo else tk.DISABLED)

    def limparCampos():
        entradaCpf.delete(0, tk.END)
        entradaRg.delete(0, tk.END)
        entradaArquivoPdf.delete(0, tk.END)
        entradaPastaDestino.delete(0, tk.END)

    def selecionarArquivoPdf():
        app.caminhoArquivoPdf = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        entradaArquivoPdf.delete(0, tk.END)
        entradaArquivoPdf.insert(0, app.caminhoArquivoPdf)

    def selecionarPastaDestino():
        app.pastaDestino = filedialog.askdirectory()
        entradaPastaDestino.delete(0, tk.END)
        entradaPastaDestino.insert(0, app.pastaDestino)

    rotuloTitulo = tk.Label(app, text="Mascarar LGPD")
    rotuloTitulo.grid(row=0, column=0, columnspan=4, pady=(10, 5))

    rotuloCpf = tk.Label(app, text="CPF:")
    rotuloCpf.grid(row=1, column=0, sticky="w", padx=10, pady=5)
    entradaCpf = tk.Entry(app, width=40)
    desfazerRefazerCpf = desfazerRefazer(entradaCpf)
    entradaCpf.grid(row=1, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

    checkboxCpf = tk.Checkbutton(app, text="Ativo", command=ativarCpf)
    checkboxCpf.grid(row=1, column=3, padx=10, pady=5)
    checkboxCpf.select()

    rotuloRg = tk.Label(app, text="RG:")
    rotuloRg.grid(row=2, column=0, sticky="w", padx=10, pady=5)
    entradaRg = tk.Entry(app, width=40)
    desfazerRefazerRg = desfazerRefazer(entradaRg)
    entradaRg.grid(row=2, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

    checkboxRg = tk.Checkbutton(app, text="Ativo", command=ativarRg)
    checkboxRg.grid(row=2, column=3, padx=10, pady=5)
    checkboxRg.select()

    rotuloArquivoPdf = tk.Label(app, text="Arquivo PDF:")
    rotuloArquivoPdf.grid(row=3, column=0, sticky="w", padx=10, pady=5)
    entradaArquivoPdf = tk.Entry(app, width=40)
    entradaArquivoPdf.grid(row=3, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

    botaoArquivoPdf = tk.Button(app, text="Selecionar", command=selecionarArquivoPdf)
    botaoArquivoPdf.grid(row=3, column=3, pady=5)

    rotuloPastaDestino = tk.Label(app, text="Pasta de destino:")
    rotuloPastaDestino.grid(row=4, column=0, sticky="w", padx=10, pady=5)
    entradaPastaDestino = tk.Entry(app, width=40)
    entradaPastaDestino.grid(row=4, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

    botaoPastaDestino = tk.Button(app, text="Selecionar", command=selecionarPastaDestino)
    botaoPastaDestino.grid(row=4, column=3, pady=5)

    botaoMascarar = tk.Button(app, text="Mascarar", command=lambda:mascarar(app, app.caminhoArquivoPdf, app.pastaDestino, app.cpfAtivo, app.rgAtivo), width=10)
    botaoMascarar.grid(row=5, column=2, sticky="e", padx=10, pady=5)

    botaoLimpar = tk.Button(app, text="Limpar", command=limparCampos, width=10)
    botaoLimpar.grid(row=5, column=3, sticky="e", pady=5)

    app.mainloop()