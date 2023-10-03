import tkinter as tk
from tkinter import filedialog, messagebox
import os.path
import mascararLGPD.pdf_mascarar as pdf_mascarar

caminho_arquivo = ""
destino = ""
cpf_ativo = True
rg_ativo = True

def ativar_cpf():
    global cpf_ativo
    cpf_ativo = not cpf_ativo
    entrada_cpf.config(state=tk.NORMAL if cpf_ativo else tk.DISABLED)

def ativar_rg():
    global rg_ativo
    rg_ativo = not rg_ativo
    entrada_rg.config(state=tk.NORMAL if rg_ativo else tk.DISABLED)

def limpar_campos():
    entrada_cpf.delete(0, tk.END)
    entrada_rg.delete(0, tk.END)
    entrada_arquivo_pdf.delete(0, tk.END)
    entrada_pasta_destino.delete(0, tk.END)

def mascarar():
    global caminho_arquivo, destino, cpf_ativo, rg_ativo

    cpf = entrada_cpf.get()
    rg = entrada_rg.get()

    if not cpf_ativo and not rg_ativo:
        messagebox.showerror("Erro", "Por favor, selecione pelo menos CPF ou RG.")
        return

    if not os.path.isfile(caminho_arquivo):
        messagebox.showerror("Erro", "O arquivo selecionado não existe.")
        return

    resultado = pdf_mascarar.mascarar(caminho_arquivo, destino, cpf_ativo, rg_ativo, cpf, rg)

    if resultado:
        messagebox.showinfo("Sucesso", resultado)
    else:
        messagebox.showinfo("Informação", "Nenhum dado encontrado para remoção.")

def selecionar_arquivo_pdf():
    global caminho_arquivo
    caminho_arquivo_pdf = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    entrada_arquivo_pdf.delete(0, tk.END)
    entrada_arquivo_pdf.insert(0, caminho_arquivo_pdf)
    caminho_arquivo = caminho_arquivo_pdf

def selecionar_pasta_destino():
    global destino
    pasta_destino = filedialog.askdirectory()
    entrada_pasta_destino.delete(0, tk.END)
    entrada_pasta_destino.insert(0, pasta_destino)
    destino = pasta_destino

raiz = tk.Tk()
raiz.title("Mascarar LGPD")
raiz.geometry("650x250")

rotulo_titulo = tk.Label(raiz, text="Mascarar LGPD")
rotulo_titulo.grid(row=0, column=0, columnspan=4, pady=(10, 5))

rotulo_cpf = tk.Label(raiz, text="CPF:")
rotulo_cpf.grid(row=1, column=0, sticky="w", padx=10, pady=5)
entrada_cpf = tk.Entry(raiz, width=40)
entrada_cpf.grid(row=1, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

checkbox_cpf = tk.Checkbutton(raiz, text="Ativo", command=ativar_cpf)
checkbox_cpf.grid(row=1, column=3, padx=10, pady=5)
checkbox_cpf.select()

rotulo_rg = tk.Label(raiz, text="RG:")
rotulo_rg.grid(row=2, column=0, sticky="w", padx=10, pady=5)
entrada_rg = tk.Entry(raiz, width=40)
entrada_rg.grid(row=2, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

checkbox_rg = tk.Checkbutton(raiz, text="Ativo", command=ativar_rg)
checkbox_rg.grid(row=2, column=3, padx=10, pady=5)
checkbox_rg.select()

rotulo_arquivo_pdf = tk.Label(raiz, text="Arquivo PDF:")
rotulo_arquivo_pdf.grid(row=3, column=0, sticky="w", padx=10, pady=5)
entrada_arquivo_pdf = tk.Entry(raiz, width=40)
entrada_arquivo_pdf.grid(row=3, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

botao_arquivo_pdf = tk.Button(raiz, text="Selecionar", command=selecionar_arquivo_pdf)
botao_arquivo_pdf.grid(row=3, column=3, pady=5)

rotulo_pasta_destino = tk.Label(raiz, text="Pasta de destino:")
rotulo_pasta_destino.grid(row=4, column=0, sticky="w", padx=10, pady=5)
entrada_pasta_destino = tk.Entry(raiz, width=40)
entrada_pasta_destino.grid(row=4, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

botao_pasta_destino = tk.Button(raiz, text="Selecionar", command=selecionar_pasta_destino)
botao_pasta_destino.grid(row=4, column=3, pady=5)

botao_mascarar = tk.Button(raiz, text="Mascarar", command=mascarar, width=10)
botao_mascarar.grid(row=5, column=2, sticky="e", padx=10, pady=5)

botao_limpar = tk.Button(raiz, text="Limpar", command=limpar_campos, width=10)
botao_limpar.grid(row=5, column=3, sticky="e", pady=5)

raiz.mainloop()
