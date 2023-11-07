from utils.imports import tk

def criarBotoes(app, texto, comando, width, row, column, sticky='ew', padx=0, pady=0):
    botoes = tk.Button(app, text=texto, command=comando, width=width)
    botoes.grid(row=row, column=column, sticky=sticky, padx=padx, pady=pady)

    return botoes