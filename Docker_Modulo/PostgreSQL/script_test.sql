-- Criação do banco de dados
CREATE DATABASE teste_db;

-- Conectar ao banco de dados criado
\c teste_db;

-- Criação de uma tabela
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    idade INT
);

-- Inserção de dados na tabela
INSERT INTO usuarios (nome, email, idade) VALUES
('João Silva', 'joao.silva@email.com', 30),
('Maria Oliveira', 'maria.oliveira@email.com', 25),
('Carlos Santos', 'carlos.santos@email.com', 40);

-- Consulta dos dados inseridos
SELECT * FROM usuarios;

-- Consulta com filtro
SELECT * FROM usuarios WHERE idade > 30;