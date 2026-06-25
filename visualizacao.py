import importacao 

arquivo_body, arquivo_title = importacao.dados()

def exibir_cabecalho():
        print(", ".join(arquivo_title))

def exibir_primeiros_passageiros():
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

def exibir_todos_dados():
    exibir_cabecalho()
    i = 0
    while(i < len(arquivo_body)): # percorrer toda a matriz
        j = 0
        while(j < 12): # mostrar todas colunas
            print(f"{arquivo_body[i][j]}", end=",")
            j = j + 1
        i = i + 1
        print()