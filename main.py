from utils.imports import tk, gui, mostrarErro
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Define as variáveis para título e dimensão da aplicação a partir das variáveis de ambiente
TITLE_APP = os.getenv("TITLE_APP")
DIMENSION_APP = os.getenv("DIMENSION_APP")

try:
    if __name__ == "__main__":
        app = tk.Tk()
        app.title(TITLE_APP)
        app.geometry(DIMENSION_APP)

        gui.create_gui(app)

        app.mainloop()
except Exception as e:
    mostrarErro(f"Ocorreu um erro inesperado: {e}")
