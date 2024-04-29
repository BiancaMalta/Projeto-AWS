# Usa a imagem oficial do Python
FROM python:3.8-slim

# Instala as dependências de build
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libc-dev \
    libmariadb-dev \
    default-libmysqlclient-dev \
    pkg-config

# Define o diretório de trabalho no container
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install cryptography

# Copie o restante dos arquivos da aplicação
COPY . .

# Cria o diretório de uploads
RUN mkdir -p /app/uploads

# Aplica permissões totais à pasta de upload
RUN chmod -R 777 /app/uploads

# Expõe a porta 5000 do contêiner
EXPOSE 5000

# Define o comando padrão para iniciar o aplicativo Flask
CMD ["python", "app.py"]
