import tkinter as tk
class desfazerRefazer:
    def __init__(self, entrada):
        self.entrada = entrada
        self.texto = tk.StringVar()
        self.entrada.config(textvariable=self.texto)
        self.historico = [] # Lista para armazenar o histórico de estados do texto
        self.indice = -1    # Índice atual no histórico

# Adiciona um rastreador para detectar mudanças no texto da entrada
        self.texto.trace_add("write", self.adicionarEstado)

# Liga a função 'desfazer' à combinação de teclas 'Control-Z'
        self.entrada.bind("<Control-z>", self.desfazer)
        
# Liga a função 'refazer' à combinação de teclas 'Control-Y'        
        self.entrada.bind("<Control-y>", self.refazer)

    def adicionarEstado(self, *args):

# Esta função é chamada sempre que o texto da entrada é modificado        
        estadoAtual = self.texto.get()
        if self.historico and estadoAtual == self.historico[self.indice]:
            return  # Se o estado atual for igual ao último, não adiciona ao histórico
        self.historico = self.historico[:self.indice + 1]   # Remove estados após o índice atual
        self.historico.append(estadoAtual)  # Adiciona o estado atual ao histórico
        self.indice += 1    # Incrementa o índice para refletir o estado atual

    def desfazer(self, evento):

# Esta função é chamada quando a combinação de teclas 'Control-Z' é pressionada       
        if self.indice > 0:     # Verifica se há estados anteriores no histórico
            self.indice -= 1    # Move para o estado anterior
            self.texto.set(self.historico[self.indice])     # Define o texto como o estado anterior
            self.entrada.icursor(tk.END)    # Define o cursor no final do texto

    def refazer(self, evento):

# Esta função é chamada quando a combinação de teclas 'Control-Y' é pressionada        
        if self.indice < len(self.historico) - 1:   # Verifica se há estados posteriores no histórico
            self.indice += 1    # Move para o estado posterior
            self.texto.set(self.historico[self.indice])     # Define o texto como o estado posterior
            self.entrada.icursor(tk.END)    # Define o cursor no final do texto
