
ARQUIVO = "livros.csv"


def carregar_livros():
    livros = []

    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for livro in leitor:
                livros.append(livro)

    return livros


def salvar_livros(livros):
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        campos = ["titulo", "autor", "ano", "isbn", "status"]

        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(livros)


def cadastrar_livro(livros):
    print("\n--- CADASTRAR LIVRO ---")