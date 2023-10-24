import tkinter as tk
import gui

if __name__ == "__main__":
    app = tk.Tk()
    app.title("Mascarar LGPD")
    app.geometry("650x250")

    gui.create_gui(app)

    app.mainloop()