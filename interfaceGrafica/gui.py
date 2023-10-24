import tkinter as tk
from tkinter import filedialog, messagebox
import os.path
import mascararDados.mascararPdf as mascararPdf
from interfaceGrafica.desfazerRefazer import desfazerRefazer


def create_gui(app):

    caminhoArquivo = ""
    destino = ""

    cpfAtivo = True
    rgAtivo = True

    def ativarCpf():
        nonlocal cpfAtivo
        cpfAtivo = not cpfAtivo
        entradaCpf.config(state=tk.NORMAL if cpfAtivo else tk.DISABLED)

    def ativarRg():
        nonlocal rgAtivo
        rgAtivo = not rgAtivo
        entradaRg.config(state=tk.NORMAL if rgAtivo else tk.DISABLED)

    def limparCampos():
        entradaCpf.delete(0, tk.END)
        entradaRg.delete(0, tk.END)
        entradaArquivoPdf.delete(0, tk.END)
        entradaPastaDestino.delete(0, tk.END)

    def mascarar():
        nonlocal caminhoArquivo, destino, cpfAtivo, rgAtivo, entradaCpf, entradaRg

        cpf = entradaCpf.get()
        rg = entradaRg.get()

        if not cpfAtivo and not rgAtivo:
            messagebox.showerror("Erro", "Por favor, selecione pelo menos CPF ou RG.")
            return  

        if not os.path.isfile(caminhoArquivo):
            messagebox.showerror("Erro", "O arquivo selecionado não existe.")
            return  

        resultado = mascararPdf.mascarar(caminhoArquivo, destino, cpfAtivo, rgAtivo, cpf, rg, entradaCpf, entradaRg)

        messagebox.showinfo("Resultado", resultado)

    def selecionarArquivoPdf():
        nonlocal caminhoArquivo
        caminhoArquivoPdf = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        entradaArquivoPdf.delete(0, tk.END)
        entradaArquivoPdf.insert(0, caminhoArquivoPdf)
        caminhoArquivo = caminhoArquivoPdf

    def selecionarPastaDestino():
        nonlocal destino
        pastaDestino = filedialog.askdirectory()
        entradaPastaDestino.delete(0, tk.END)
        entradaPastaDestino.insert(0, pastaDestino)
        destino = pastaDestino

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

    botaoMascarar = tk.Button(app, text="Mascarar", command=mascarar, width=10)
    botaoMascarar.grid(row=5, column=2, sticky="e", padx=10, pady=5)

    botaoLimpar = tk.Button(app, text="Limpar", command=limparCampos, width=10)
    botaoLimpar.grid(row=5, column=3, sticky="e", pady=5)

    app.mainloop()