import tkinter as tk
import re
import os
import os.path
import fitz
import mascararDados.mascararPdf as mascararPdf
import interfaceGrafica.gui as gui
from tkinter import messagebox, filedialog
from utils.tratamentoErros import mostrarErro, mostrarAviso, mostrarInfo
from ..mascararDados.mascararCpf import removerCpf
from ..mascararDados.mascararRg import removerRg
from ..interfaceGrafica.funcoesAuxiliares.mascarar import mascarar
from ..interfaceGrafica.funcoesAuxiliares.desfazerRefazer import desfazerRefazer
from ..interfaceGrafica.funcoesAuxiliares.selecionarArquivoPdf import selecionarArquivoPdf
from ..interfaceGrafica.funcoesAuxiliares.selecionarPastaDestino import selecionarPastaDestino
from ..interfaceGrafica.funcoesAuxiliares.ativarCampo import ativarCampo
from ..interfaceGrafica.funcoesAuxiliares.limparCampos import limparCampos
from ..interfaceGrafica.componentes.rotulo import criarRotulo
from ..interfaceGrafica.componentes.campoTexto import criarCampoTexto
from ..interfaceGrafica.componentes.checkBox import criarCheckBox
from ..interfaceGrafica.componentes.botoes import criarBotoes