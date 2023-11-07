from utils.imports import tk

def ativarCampo(app, campo, entrada):
    if campo == "CPF":
        app.cpfAtivo = not app.cpfAtivo
        entrada.config(state=tk.NORMAL if app.cpfAtivo else tk.DISABLED)
    elif campo == "RG":
        app.rgAtivo = not app.rgAtivo
        entrada.config(state=tk.NORMAL if app.rgAtivo else tk.DISABLED)
