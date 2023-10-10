import tkinter as tk

class desfazerRefazer:  # Nome da classe ajustada
    def __init__(self, entrada):
        self.entrada = entrada
        self.texto = tk.StringVar()
        self.entrada.config(textvariable=self.texto)
        self.historico = []
        self.indice = -1

        self.texto.trace_add("write", self.adicionarEstado)
        self.entrada.bind("<Control-z>", self.desfazer)
        self.entrada.bind("<Control-y>", self.refazer)

    def adicionarEstado(self, *args):
        estadoAtual = self.texto.get()
        if self.historico and estadoAtual == self.historico[self.indice]:
            return
        self.historico = self.historico[:self.indice + 1]
        self.historico.append(estadoAtual)
        self.indice += 1

    def desfazer(self, evento):
        if self.indice > 0:
            self.indice -= 1
            self.texto.set(self.historico[self.indice])
            self.entrada.icursor(tk.END)

    def refazer(self, evento):
        if self.indice < len(self.historico) - 1:
            self.indice += 1
            self.texto.set(self.historico[self.indice])
            self.entrada.icursor(tk.END)
