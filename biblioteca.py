import csv

NOME_ARQUIVO = "livros.csv"


def carregar_livros():
    livros = []

    try:
        with open(NOME_ARQUIVO, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for livro in leitor:
                livros.append(livro)

    except FileNotFoundError:
        pass

    return livros
def salvar_livros(livros):
    with open(NOME_ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        campos = ["titulo", "autor", "ano", "codigo", "status"]

        escritor = csv.DictWriter(arquivo, fieldnames=campos)

        escritor.writeheader()
        escritor.writerows(livros)