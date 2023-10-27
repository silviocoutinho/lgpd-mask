import tkinter as tk
from .funcoesAuxiliares.desfazerRefazer import desfazerRefazer
from .funcoesAuxiliares.mascarar import mascarar
from .funcoesAuxiliares.selecionarArquivoPdf import selecionarArquivoPdf
from .selecionarPastaDestino import selecionarPastaDestino
from .funcoesAuxiliares.ativarCpf import ativarCpf
from .funcoesAuxiliares.ativarRg import ativarRg
from .funcoesAuxiliares.limparCampos import limparCampos

def create_gui(app):

    app.caminhoArquivoPdf = ""
    app.pastaDestino = ""

    app.cpfAtivo = True
    app.rgAtivo = True

    def selecionarDestino():
        selecionarPastaDestino(app)

    rotuloTitulo = tk.Label(app, text="Mascarar LGPD")
    rotuloTitulo.grid(row=0, column=0, columnspan=4, pady=(10, 5))

    rotuloCpf = tk.Label(app, text="CPF:")
    rotuloCpf.grid(row=1, column=0, sticky="w", padx=10, pady=5)
    entradaCpf = tk.Entry(app, width=40)
    desfazerRefazerCpf = desfazerRefazer(entradaCpf)
    entradaCpf.grid(row=1, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

    checkboxCpf = tk.Checkbutton(app, text="Ativo", command=lambda:ativarCpf(app, entradaCpf))
    checkboxCpf.grid(row=1, column=3, padx=10, pady=5)
    checkboxCpf.select()

    rotuloRg = tk.Label(app, text="RG:")
    rotuloRg.grid(row=2, column=0, sticky="w", padx=10, pady=5)
    entradaRg = tk.Entry(app, width=40)
    desfazerRefazerRg = desfazerRefazer(entradaRg)
    entradaRg.grid(row=2, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

    checkboxRg = tk.Checkbutton(app, text="Ativo", command=lambda:ativarRg(app, entradaRg))
    checkboxRg.grid(row=2, column=3, padx=10, pady=5)
    checkboxRg.select()

    rotuloArquivoPdf = tk.Label(app, text="Arquivo PDF:")
    rotuloArquivoPdf.grid(row=3, column=0, sticky="w", padx=10, pady=5)
    entradaArquivoPdf = tk.Entry(app, width=40)
    entradaArquivoPdf.grid(row=3, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

    botaoArquivoPdf = tk.Button(app, text="Selecionar", command=lambda:selecionarArquivoPdf(app))
    botaoArquivoPdf.grid(row=3, column=3, pady=5)

    rotuloPastaDestino = tk.Label(app, text="Pasta de destino:")
    rotuloPastaDestino.grid(row=4, column=0, sticky="w", padx=10, pady=5)
    entradaPastaDestino = tk.Entry(app, width=40)
    entradaPastaDestino.grid(row=4, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

    botaoPastaDestino = tk.Button(app, text="Selecionar", command=selecionarDestino)
    botaoPastaDestino.grid(row=4, column=3, pady=5)

    botaoMascarar = tk.Button(app, text="Mascarar", command=lambda:mascarar(app, app.caminhoArquivoPdf, app.pastaDestino, app.cpfAtivo, app.rgAtivo), width=10)
    botaoMascarar.grid(row=5, column=2, sticky="e", padx=10, pady=5)

    botaoLimpar = tk.Button(app, text="Limpar", command=lambda:limparCampos(entradaCpf, entradaRg, entradaArquivoPdf, entradaPastaDestino), width=10)
    botaoLimpar.grid(row=5, column=3, sticky="e", pady=5)

    app.mainloop()