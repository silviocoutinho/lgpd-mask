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

    criarRotulo(app, "Mascarar LGPD", 0, 2)

    criarRotulo(app, "CPF:", 1, 0)
    entradaCpf = criarCampoTexto(app, 35, 1, 1)
    criarCheckBox(app, "Ativo", 1, 3, lambda: ativarCpf(app, entradaCpf))
    desfazerRefazer(entradaCpf)

    criarRotulo(app, "RG:", 2, 0)
    entradaRg = criarCampoTexto(app, 35, 2, 1)
    criarCheckBox(app, "Ativo", 2, 3, lambda: ativarRg(app, entradaRg))
    desfazerRefazer(entradaRg)

    criarRotulo(app, "Arquivo PDF:", 3, 0)
    entradaArquivoPdf = criarCampoTexto(app, 35, 3, 1)
    desfazerRefazer(entradaArquivoPdf)

    criarRotulo(app, "Pasta de destino:", 4, 0)
    entradaPastaDestino = criarCampoTexto(app, 35, 4, 1)
    desfazerRefazer(entradaPastaDestino)

    botoes = [
        {"text": "Selecionar", "command": lambda: selecionarArquivoPdf(app), "width": 10, "row": 3, "column": 3, "sticky": "", "padx": 0, "pady": 5},
        {"text": "Selecionar", "command": lambda: selecionarPastaDestino(app), "width": 10, "row": 4, "column": 3, "sticky": "", "padx": 0, "pady": 5},
        {"text": "Mascarar", "command": lambda: mascarar(app, app.caminhoArquivoPdf, app.pastaDestino, app.cpfAtivo, app.rgAtivo), "width": 10, "row": 5, "column": 2, "sticky": "e", "padx": 10, "pady": 5},
        {"text": "Limpar", "command": lambda: limparCampos(entradaCpf, entradaRg, entradaArquivoPdf, entradaPastaDestino), "width": 10, "row": 5, "column": 3, "sticky": "e", "padx": 0, "pady": 5}
    ]

    botoesCriados = criarBotoes(app, botoes)

    app.mainloop()