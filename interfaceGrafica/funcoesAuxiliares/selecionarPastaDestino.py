from utils.imports import tk, filedialog
from utils.tratamentoErros import mostrarErroSelecaoDestino

def selecionarPastaDestino(app):
    try:
        app.pastaDestino = filedialog.askdirectory()
        if app.pastaDestino:
            entradaPastaDestino = app.children['!entry4']
            entradaPastaDestino.delete(0, tk.END)
            entradaPastaDestino.insert(0, app.pastaDestino)
        else:
            entradaPastaDestino = app.children['!entry4']
            entradaPastaDestino.delete(0, tk.END)
            entradaPastaDestino.insert(0, "")
    except Exception as e:
        mostrarErroSelecaoDestino(e)
