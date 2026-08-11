
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
     titulo = input("Digite o título: ")
    autor = input("Digite o autor: ")
    ano = input("Digite o ano de publicação: ")
    isbn = input("Digite o ISBN: ")

    for livro in livros:
        if livro["isbn"] == isbn:
            print("Esse ISBN já está cadastrado.")
            return livros

    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "isbn": isbn,
        "status": "disponível"
    }

    livros.append(livro)
    salvar_livros(livros)

    print("Livro cadastrado com sucesso!")

    return livros


def procurar_livro(livros, isbn):
    for livro in livros:
        if livro["isbn"] == isbn:
            return livro
         return None


def emprestar_livro(livros):
    print("\n--- EMPRESTAR LIVRO ---")

    isbn = input("Digite o ISBN do livro: ")

    livro = procurar_livro(livros, isbn)

    if livro is None:
        print("Livro não encontrado.")
        return livros

    if livro["status"] == "emprestado":
        print("Esse livro já está emprestado.")
        return livros

    livro["status"] = "emprestado"
    salvar_livros(livros)

    print("Livro emprestado com sucesso!")

    return livros


def devolver_livro(livros):
    print("\n--- DEVOLVER LIVRO ---")

    isbn = input("Digite o ISBN do livro: ")

    livro = procurar_livro(livros, isbn)

    if livro is None:
        print("Livro não encontrado.")
        return livros

    if livro["status"] == "disponível":
        print("Esse livro já está disponível.")
        return livros

    livro["status"] = "disponível"
    salvar_livros(livros)

    print("Livro devolvido com sucesso!")

        