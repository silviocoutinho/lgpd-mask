from utils.imports import messagebox

def mostrarErro(mensagem):
    messagebox.showerror("Erro", mensagem)

def mostrarAviso(mensagem):
    messagebox.showwarning("Aviso", mensagem)

def mostrarInfo(mensagem):
    messagebox.showinfo("Informação", mensagem)