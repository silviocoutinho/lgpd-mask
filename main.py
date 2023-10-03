import tkinter as tk
from tkinter import filedialog, messagebox
import fitz
import os.path
import re

# Variáveis globais para armazenar o caminho do arquivo PDF e a pasta de destino
caminhoArquivo = ""
destino = ""

# Variáveis globais para controlar se CPF e RG estão habilitados
cpf_enabled = True
rg_enabled = True

# Função para alternar a habilitação do campo CPF
def toggle_cpf():
    global cpf_enabled
    cpf_enabled = not cpf_enabled
    cpf_entry.config(state=tk.NORMAL if cpf_enabled else tk.DISABLED)

# Função para alternar a habilitação do campo RG
def toggle_rg():
    global rg_enabled
    rg_enabled = not rg_enabled
    rg_entry.config(state=tk.NORMAL if rg_enabled else tk.DISABLED)

# Função para limpar os campos de entrada
def clear_button():
    cpf_entry.delete(0, tk.END)
    rg_entry.delete(0, tk.END)
    pdf_file_entry.delete(0, tk.END)
    dest_folder_entry.delete(0, tk.END)

# Função principal para mascarar dados
def mask():
    global cpf_enabled, rg_enabled
    cpf = cpf_entry.get()
    rg = rg_entry.get()

    # Verificações iniciais
    if not cpf_enabled and not rg_enabled:
        messagebox.showerror("Erro", "Por favor, selecione pelo menos CPF ou RG.")
        return  # Não continue se ambos estiverem desativados
    elif not os.path.isfile(caminhoArquivo):
        messagebox.showerror("Erro", "O arquivo selecionado não existe.")
        return  # Não continue se o arquivo não existir

    arquivo = caminhoArquivo
    doc = fitz.open(arquivo)
    achouCPF = False
    achouRG = False
    mensagem = []

    # Remove caracteres não numéricos do CPF e RG fornecidos
    cpf_digitos = re.sub(r'\D', '', cpf)
    rg_cleaned = re.sub(r'\D', '', rg)

    # Processa CPF
    if cpf_enabled and cpf:
        cpf_pattern = re.compile(r'CPF\s*n[°ºº.]*\s*([\d]{3}[-.\s]?[\d]{3}[-.\s]?[\d]{3}[-.\s]?\s?[\d]{2})')
        for page in doc:
            text = page.get_text()
            cpf_matches = cpf_pattern.findall(text)

            for match in cpf_matches:
                cpf_pdf = re.sub(r'\D', '', match)
                if cpf_pdf == cpf_digitos:
                    rect = page.search_for(match)
                    for r in rect:
                        a = page.add_redact_annot(r, fill=(0, 0, 0))
                        a.update()
                        page.apply_redactions()
                    achouCPF = True
                    mensagem.append("CPF removido com sucesso.")
                    cpf_entry.delete(0, tk.END)

    # Processa RG
    if rg_enabled and rg:
        rg_pattern = re.compile(r'RG\s*n[°ºº.]*\s*((?:[A-Z]+\s*)?[-.\s]?\s*[\d.-]+(?:\s*[–-]\s*[A-Z/]+[A-Z/]+)?)')
        for page in doc:
            text = page.get_text()
            rg_matches = rg_pattern.findall(text)

            for match in rg_matches:
                rg_pdf = re.sub(r'\D', '', match)
                if rg_pdf == rg_cleaned:
                    rect = page.search_for(match)
                    for r in rect:
                        a = page.add_redact_annot(r, fill=(0, 0, 0))
                        a.update()
                        page.apply_redactions()
                    achouRG = True
                    mensagem.append("RG removido com sucesso.")
                    rg_entry.delete(0, tk.END)

    # Exibe mensagens de resultado
    if mensagem:
        mensagem_final = []
        if achouCPF:
            mensagem_final.append("CPF removido com sucesso.")
        if achouRG:
            mensagem_final.append("RG removido com sucesso.")
        
        nome_arquivo_destino = os.path.basename(caminhoArquivo)
        caminho_destino = os.path.join(destino, nome_arquivo_destino)
        doc.save(caminho_destino)
        
        messagebox.showinfo("Sucesso", "\n".join(mensagem_final))
    else:
        messagebox.showinfo("Informação", "Nenhum dado encontrado para remoção.")

# Função para selecionar um arquivo PDF
def select_pdf_file():
    global caminhoArquivo
    pdf_file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    pdf_file_entry.delete(0, tk.END)
    pdf_file_entry.insert(0, pdf_file_path)
    caminhoArquivo = pdf_file_path

# Função para selecionar uma pasta de destino
def select_destination_folder():
    global destino
    dest_folder_path = filedialog.askdirectory()
    dest_folder_entry.delete(0, tk.END)
    dest_folder_entry.insert(0, dest_folder_path)
    destino = dest_folder_path

# Criação da interface gráfica usando Tkinter
root = tk.Tk()
root.title("Mascarar LGPD")
root.geometry("650x250")  

# Rótulo do título
title_label = tk.Label(root, text="Mascarar LGPD")
title_label.grid(row=0, column=0, columnspan=4, pady=(10, 5))

# Rótulo e campo de entrada para CPF
cpf_label = tk.Label(root, text="CPF:")
cpf_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
cpf_entry = tk.Entry(root, width=40)
cpf_entry.grid(row=1, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

# Checkbox para habilitar/desabilitar CPF
cpf_checkbox = tk.Checkbutton(root, text="Ativo", command=toggle_cpf)
cpf_checkbox.grid(row=1, column=3, padx=10, pady=5)
cpf_checkbox.select()

# Rótulo e campo de entrada para RG
rg_label = tk.Label(root, text="RG:")
rg_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)
rg_entry = tk.Entry(root, width=40)
rg_entry.grid(row=2, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

# Checkbox para habilitar/desabilitar RG
rg_checkbox = tk.Checkbutton(root, text="Ativo", command=toggle_rg)
rg_checkbox.grid(row=2, column=3, padx=10, pady=5)
rg_checkbox.select()

# Rótulo e campo de entrada para o arquivo PDF
pdf_file_label = tk.Label(root, text="Arquivo PDF:")
pdf_file_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)
pdf_file_entry = tk.Entry(root, width=40)
pdf_file_entry.grid(row=3, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

# Botão para selecionar um arquivo PDF
pdf_file_button = tk.Button(root, text="Selecionar", command=select_pdf_file)
pdf_file_button.grid(row=3, column=3, pady=5)

# Rótulo e campo de entrada para a pasta de destino
dest_folder_label = tk.Label(root, text="Pasta de destino:")
dest_folder_label.grid(row=4, column=0, sticky="w", padx=10, pady=5)
dest_folder_entry = tk.Entry(root, width=40)
dest_folder_entry.grid(row=4, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

# Botão para selecionar uma pasta de destino
dest_folder_button = tk.Button(root, text="Selecionar", command=select_destination_folder)
dest_folder_button.grid(row=4, column=3, pady=5)

# Botão para mascarar os dados
mask_button = tk.Button(root, text="Mascarar", command=mask, width=10)
mask_button.grid(row=5, column=2, sticky="e", padx=10, pady=5)

# Botão para limpar os campos de entrada
clear_button = tk.Button(root, text="Limpar", command=clear_button, width=10)
clear_button.grid(row=5, column=3, sticky="e", pady=5)

# Iniciar a interface gráfica
root.mainloop()
