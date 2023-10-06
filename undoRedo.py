import tkinter as tk

class UndoRedoManager:
    def __init__(self, entry):
        self.entry = entry
        self.text = tk.StringVar()
        self.entry.config(textvariable=self.text)
        self.history = []
        self.index = -1

        self.text.trace_add("write", self.add_state)
        self.entry.bind("<Control-z>", self.undo)
        self.entry.bind("<Control-y>", self.redo)

    def add_state(self, *args):
        current_state = self.text.get()
        if self.history and current_state == self.history[self.index]:
            return
        self.history = self.history[:self.index + 1]
        self.history.append(current_state)
        self.index += 1

    def undo(self, event):
        if self.index > 0:
            self.index -= 1
            self.text.set(self.history[self.index])
            self.entry.icursor(tk.END)

    def redo(self, event):
        if self.index < len(self.history) - 1:
            self.index += 1
            self.text.set(self.history[self.index])
            self.entry.icursor(tk.END)
