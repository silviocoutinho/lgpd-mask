from utils.imports import tk, gui, mostrarErro

try:
    if __name__ == "__main__":
        app = tk.Tk()
        app.title("Mascarar LGPD")
        app.geometry("650x250")

        gui.create_gui(app)

        app.mainloop()
except Exception as e:
    mostrarErro(f"Ocorreu um erro inesperado: {e}")