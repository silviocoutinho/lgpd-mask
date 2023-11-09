FROM python:3.8

WORKDIR /app

COPY . /app

# Instalando dependências
RUN pip install -r requirements.txt

# Comando padrão para executar o script principal
CMD ["python", "main.py"]
