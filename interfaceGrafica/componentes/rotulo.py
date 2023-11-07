from utils.imports import tk

def criarRotulo(app, texto, row, column, sticky='w', padx=10, pady=5, columnspan=1):
    rotulo = tk.Label(app, text=texto)
    rotulo.grid(row=row, column=column, sticky=sticky, padx=padx, pady=pady, columnspan=columnspan)
    return rotulo