from utils.imports import tk

def criarCheckBox(app, texto, row, column, comando=None):
    checkBox = tk.Checkbutton(app, text=texto, command=comando)
    checkBox.grid(row=row, column=column, padx=10, pady=5)
    checkBox.select()
    return checkBox