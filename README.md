# Sistema de Biblioteca

## Sobre o projeto

Este projeto foi feito em Python para criar um sistema simples de gerenciamento
de livros.

Com ele é possível cadastrar livros, consultar os livros cadastrados, realizar
empréstimos e devoluções e também organizar a lista de livros.

O projeto foi desenvolvido para praticar alguns conceitos básicos de Python,
como funções, listas, dicionários, condições, repetições e arquivos.

## O que o programa faz

- Cadastra livros novos.
- Mostra os livros cadastrados.
- Procura livros pelo título ou pelo autor.
- Faz o registro de empréstimos.
- Faz o registro de devoluções.
- Permite organizar os livros por título, autor ou ano.
- Salva os livros em um arquivo.
- Recupera os livros salvos quando o programa é iniciado.

## Menu do programa

Quando o programa começa, aparece um menu com algumas opções.

O usuário pode escolher:

1. Cadastrar livro
2. Emprestar livro
3. Devolver livro
4. Listar livros
5. Buscar livro
6. Ordenar livros
7. Sair

As informações dos livros ficam salvas no arquivo `livros.txt`. Dessa forma,
quando o programa for fechado, os livros cadastrados não são perdidos.

## Informações de cada livro

Cada livro cadastrado possui:

- Título
- Autor
- Ano
- Código ou ISBN
- Status

O status mostra se o livro está:

- Disponível
- Emprestado

## Ferramentas utilizadas

- Python
- Visual Studio Code
- Arquivo de texto (`livros.txt`)

## Como executar o programa

1. Ter o Python instalado no computador.
2. Abrir a pasta do projeto no Visual Studio Code.
3. Abrir o terminal do VS Code.
4. Executar o comando:

```bash
python biblioteca.py
 