-- Cria o banco de dados se não existir
CREATE DATABASE IF NOT EXISTS arquivos;

-- Usa o banco de dados
USE arquivos;

-- Cria a tabela de relatórios
CREATE TABLE IF NOT EXISTS Report (
    id INT AUTO_INCREMENT PRIMARY KEY,
    filename VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (filename)  -- Adiciona um índice único no campo filename
);

-- Insere alguns dados de exemplo na tabela de relatórios
INSERT INTO Report
  (filename, username)
VALUES
  ('relatorio1.pdf', 'admin'),
  ('relatorio2.pdf', 'usuario1');

