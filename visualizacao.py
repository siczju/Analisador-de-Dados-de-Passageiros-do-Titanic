def exibir_cabecalho(arquivo_title):
    """
    Exibe o cabeçalho com os nomes das colunas da base.

    Parâmetros:
    - arquivo_title (list): Lista com os nomes das colunas do Titanic.

    Retorno:
    - None: exibe na tela os nomes das colunas separados por vírgula.
    """
    print(", ".join(arquivo_title))

def exibir_primeiros_passageiros(arquivo_body):
    """
    Exibe os dados dos 5 primeiros passageiros da base.

    Parâmetros:
    - arquivo_body (list): Lista de listas contendo os dados do Titanic.

    Retorno:
    - None: exibe na tela as 12 colunas das cinco primeiras linhas.
    """
    i = 0
    while(i < 5): # percorrer ate o 5
        j = 0
        while(j < 12): # mostrar todas colunas
            if j == 11:
                 print(f"{arquivo_body[i][j]}", end="")
            else:
                print(f"{arquivo_body[i][j]}", end=",")
            j = j + 1
        i = i + 1
        print()

def exibir_todos_dados(arquivo_body, arquivo_title):
    """
    Lista todos os passageiros da base, com o cabeçalho no topo.

    Parâmetros:
    - arquivo_body (list): Lista de listas contendo os dados do Titanic.
    - arquivo_title (list): Lista com os nomes das colunas do Titanic.

    Retorno:
    - None: exibe na tela o cabeçalho e todas as linhas de passageiros.
    """
    exibir_cabecalho(arquivo_title)
    i = 0
    while(i < len(arquivo_body)): # percorrer toda a matriz
        j = 0
        while(j < 12): # mostrar todas colunas
            print(f"{arquivo_body[i][j]}", end=",")
            j = j + 1
        i = i + 1
        print()
