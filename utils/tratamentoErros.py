from utils.imports import tk
from .mensagens import erroInesperado, erroSelecaoDestino, erroSelecaoArquivo, arquivoInvalido, arquivoNaoExiste, selecioneCampo, encontrado, naoEncontrado

def mostrarErroInesperado(e):
    tk.messagebox.showerror("Erro Inesperado", erroInesperado(e))

def mostrarErroSelecaoDestino(e):
    tk.messagebox.showerror("Erro na Seleção do Destino", erroSelecaoDestino(e))

def mostrarErroSelecaoArquivo(e):
    tk.messagebox.showerror("Erro na Seleção do Arquivo", erroSelecaoArquivo(e))

def mostrarArquivoInvalido():
    tk.messagebox.showinfo("Arquivo Inválido", arquivoInvalido())

def mostrarArquivoInexistente():
    tk.messagebox.showinfo("Arquivo Inexistente", arquivoNaoExiste())

def mostrarSelecaoCampo(campo):
    tk.messagebox.showinfo("Seleção de Campo", selecioneCampo(campo))

def mostrarEncontrado(campo):
    tk.messagebox.showinfo("Encontrado", encontrado(campo))

def mostrarNaoEncontrado(campo):
    tk.messagebox.showinfo("Não Encontrado", naoEncontrado(campo))