from utils.imports import tk, filedialog
from utils.tratamentoErros import mostrarArquivoInvalido, mostrarErroSelecaoArquivo, mostrarArquivoInexistente

def selecionarArquivoPdf(app):
    try:
        app.caminhoArquivoPdf = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if app.caminhoArquivoPdf:
            if not app.caminhoArquivoPdf.lower().endswith(".pdf"):
                mostrarArquivoInvalido()
            else:        
                entradaArquivoPdf = app.children['!entry3']
                entradaArquivoPdf.delete(0, tk.END)
                entradaArquivoPdf.insert(0, app.caminhoArquivoPdf)
        else:
            mostrarArquivoInexistente()
    except Exception as e:
        mostrarErroSelecaoArquivo(e)
