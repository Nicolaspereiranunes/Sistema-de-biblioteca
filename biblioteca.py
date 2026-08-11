
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
      return livros


def listar_livros(livros):
    print("\n--- LIVROS CADASTRADOS ---")

    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return livros

    for i, livro in enumerate(livros, 1):
        print("\nLivro", i)
        print("Título:", livro["titulo"])
        print("Autor:", livro["autor"])
        print("Ano:", livro["ano"])
        print("ISBN:", livro["isbn"])
        print("Status:", livro["status"])

    return livros


def buscar_livro(livros):
    print("\n--- BUSCAR LIVRO ---")

    pesquisa = input("Digite o título ou autor: ").lower()

    encontrados = []

    for livro in livros:
        if pesquisa in livro["titulo"].lower() or pesquisa in livro["autor"].lower():
            encontrados.append(livro)

    if len(encontrados) == 0:
        print("Nenhum livro encontrado.")
    else:
        print("\nLivros encontrados:")

        for livro in encontrados:
            print(
                livro["titulo"],
                "-",
                livro["autor"],
                "-",
                livro["ano"],
                "-",
                livro["status"]
            )
                return encontrados


def ordenar_livros(livros):
    print("\n--- ORDENAR LIVROS ---")
    print("1 - Título")
    print("2 - Autor")
    print("3 - Ano")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        livros.sort(key=lambda livro: livro["titulo"].lower())
        print("Livros ordenados por título.")

    elif opcao == "2":
        livros.sort(key=lambda livro: livro["autor"].lower())
        print("Livros ordenados por autor.")

    elif opcao == "3":
        livros.sort(key=lambda livro: int(livro["ano"]))
        print("Livros ordenados por ano.")

    else:
        print("Opção inválida.")

    return livros


def menu():
    print("\n==============================")
    print("      MINHA BIBLIOTECA")
    print("==============================")
    print("1 - Cadastrar livro")
    print("2 - Emprestar livro")
    print("3 - Devolver livro")
    print("4 - Listar livros")
    print("5 - Buscar livro")
    print("6 - Ordenar livros")
    print("7 - Sair")
    print("==============================")


livros = carregar_livros()

while True:
    menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        livros = cadastrar_livro(livros)

    elif opcao == "2":
        livros = emprestar_livro(livros)

    elif opcao == "3":
        livros = devolver_livro(livros)

    elif opcao == "4":
        listar_livros(livros)

    elif opcao == "5":
        buscar_livro(livros)

    elif opcao == "6":
        livros = ordenar_livros(livros)
        salvar_livros(livros)

    elif opcao == "7":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")

        