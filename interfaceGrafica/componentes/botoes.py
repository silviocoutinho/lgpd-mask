import tkinter as tk 

def criarBotoes(app, botoes):
    criados = []
    for config in botoes:
        botao = tk.Button(app, text=config['text'], command=config['command'], width=config['width'])
        botao.grid(row=config['row'], column=config['column'], sticky=config['sticky'], padx=config['padx'], pady=config['pady'])
        criados.append(botao)
    return criados