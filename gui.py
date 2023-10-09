import tkinter as tk
from tkinter import filedialog, messagebox
import os.path
import mascararDados.mascararPdf as mascararPdf
from undoRedo import UndoRedoManager


def create_gui(app):
    caminhoArquivo = ""
    destino = ""
    cpfAtivo = True
    rg_ativo = True

    def ativarCpf():
        nonlocal cpfAtivo
        cpfAtivo = not cpfAtivo
        entrada_cpf.config(state=tk.NORMAL if cpfAtivo else tk.DISABLED)

    def ativar_rg():
        nonlocal rg_ativo
        rg_ativo = not rg_ativo
        entrada_rg.config(state=tk.NORMAL if rg_ativo else tk.DISABLED)

    def limpar_campos():
        entrada_cpf.delete(0, tk.END)
        entrada_rg.delete(0, tk.END)
        entradaArquivoPdf.delete(0, tk.END)
        entrada_pasta_destino.delete(0, tk.END)

    def mascarar():
        nonlocal caminhoArquivo, destino, cpfAtivo, rg_ativo, entrada_cpf, entrada_rg

        cpf = entrada_cpf.get()
        rg = entrada_rg.get()

        if not cpfAtivo and not rg_ativo:
            messagebox.showerror("Erro", "Por favor, selecione pelo menos CPF ou RG.")
            return

        if not os.path.isfile(caminhoArquivo):
            messagebox.showerror("Erro", "O arquivo selecionado não existe.")
            return

        resultado = mascararPdf.mascarar(caminhoArquivo, destino, cpfAtivo, rg_ativo, cpf, rg, entrada_cpf, entrada_rg)

        messagebox.showinfo("Resultado", resultado)

    def selecionar_arquivo_pdf():
        nonlocal caminhoArquivo
        caminhoArquivoPdf = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        entradaArquivoPdf.delete(0, tk.END)
        entradaArquivoPdf.insert(0, caminhoArquivoPdf)
        caminhoArquivo = caminhoArquivoPdf

    def selecionar_pasta_destino():
        nonlocal destino
        pasta_destino = filedialog.askdirectory()
        entrada_pasta_destino.delete(0, tk.END)
        entrada_pasta_destino.insert(0, pasta_destino)
        destino = pasta_destino

    rotulo_titulo = tk.Label(app, text="Mascarar LGPD")
    rotulo_titulo.grid(row=0, column=0, columnspan=4, pady=(10, 5))

    rotulo_cpf = tk.Label(app, text="CPF:")
    rotulo_cpf.grid(row=1, column=0, sticky="w", padx=10, pady=5)
    entrada_cpf = tk.Entry(app, width=40)
    undo_redo_cpf = UndoRedoManager(entrada_cpf)
    entrada_cpf.grid(row=1, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

    checkbox_cpf = tk.Checkbutton(app, text="Ativo", command=ativarCpf)
    checkbox_cpf.grid(row=1, column=3, padx=10, pady=5)
    checkbox_cpf.select()

    rotulo_rg = tk.Label(app, text="RG:")
    rotulo_rg.grid(row=2, column=0, sticky="w", padx=10, pady=5)
    entrada_rg = tk.Entry(app, width=40)
    undo_redo_rg = UndoRedoManager(entrada_rg)
    entrada_rg.grid(row=2, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

    checkbox_rg = tk.Checkbutton(app, text="Ativo", command=ativar_rg)
    checkbox_rg.grid(row=2, column=3, padx=10, pady=5)
    checkbox_rg.select()

    rotulo_arquivo_pdf = tk.Label(app, text="Arquivo PDF:")
    rotulo_arquivo_pdf.grid(row=3, column=0, sticky="w", padx=10, pady=5)
    entradaArquivoPdf = tk.Entry(app, width=40)
    entradaArquivoPdf.grid(row=3, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

    botao_arquivo_pdf = tk.Button(app, text="Selecionar", command=selecionar_arquivo_pdf)
    botao_arquivo_pdf.grid(row=3, column=3, pady=5)

    rotulo_pasta_destino = tk.Label(app, text="Pasta de destino:")
    rotulo_pasta_destino.grid(row=4, column=0, sticky="w", padx=10, pady=5)
    entrada_pasta_destino = tk.Entry(app, width=40)
    entrada_pasta_destino.grid(row=4, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

    botao_pasta_destino = tk.Button(app, text="Selecionar", command=selecionar_pasta_destino)
    botao_pasta_destino.grid(row=4, column=3, pady=5)

    botao_mascarar = tk.Button(app, text="Mascarar", command=mascarar, width=10)
    botao_mascarar.grid(row=5, column=2, sticky="e", padx=10, pady=5)

    botao_limpar = tk.Button(app, text="Limpar", command=limpar_campos, width=10)
    botao_limpar.grid(row=5, column=3, sticky="e", pady=5)

    app.mainloop()
