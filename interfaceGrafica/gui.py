import tkinter as tk
from .funcoesAuxiliares.mascarar import mascarar
from .funcoesAuxiliares.desfazerRefazer import desfazerRefazer
from .funcoesAuxiliares.selecionarArquivoPdf import selecionarArquivoPdf
from .funcoesAuxiliares.selecionarPastaDestino import selecionarPastaDestino
from .funcoesAuxiliares.ativarCpf import ativarCpf
from .funcoesAuxiliares.ativarRg import ativarRg
from .funcoesAuxiliares.limparCampos import limparCampos
from .componentes.rotulo import criarRotulo
from .componentes.campoTexto import criarCampoTexto
from .componentes.checkBox import criarCheckBox
from .componentes.botoes import criarBotoes

def create_gui(app):

    app.caminhoArquivoPdf = ""
    app.pastaDestino = ""

    app.cpfAtivo = True
    app.rgAtivo = True

    criarRotulo(app, "Mascarar LGPD", 0, 1, padx=100, columnspan=3, pady=(20, 10))

    criarRotulo(app, "CPF:", 1, 0)
    entradaCpf = criarCampoTexto(app, 40, 1, 1)
    criarCheckBox(app, "Ativo", 1, 2, lambda: ativarCpf(app, entradaCpf))
    desfazerRefazer(entradaCpf)

    criarRotulo(app, "RG:", 2, 0)
    entradaRg = criarCampoTexto(app, 40, 2, 1)
    criarCheckBox(app, "Ativo", 2, 2, lambda: ativarRg(app, entradaRg))
    desfazerRefazer(entradaRg)

    criarRotulo(app, "Arquivo PDF:", 3, 0)
    entradaArquivoPdf = criarCampoTexto(app, 40, 3, 1)
    desfazerRefazer(entradaArquivoPdf)

    criarRotulo(app, "Pasta de destino:", 4, 0)
    entradaPastaDestino = criarCampoTexto(app, 40, 4, 1)
    desfazerRefazer(entradaPastaDestino)

    selecionarPdfBtn = criarBotoes(app, "Selecionar", lambda: selecionarArquivoPdf(app), 10, 3, 2, "e", 5, 5)
    selecionarDestinoBtn = criarBotoes(app, "Selecionar", lambda: selecionarPastaDestino(app), 10, 4, 2, "e", 5, 5)
    mascararBtn = criarBotoes(app, "Mascarar", lambda: mascarar(app, app.caminhoArquivoPdf, app.pastaDestino, app.cpfAtivo, app.rgAtivo), 10, 5, 1, "e", 10, 5)
    limparBtn = criarBotoes(app, "Limpar", lambda: limparCampos(entradaCpf, entradaRg, entradaArquivoPdf, entradaPastaDestino), 10, 5, 2, "e", 5, 5)

    app.mainloop()