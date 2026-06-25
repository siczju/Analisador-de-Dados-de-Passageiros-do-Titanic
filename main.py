import importacao
import visualizacao
import analise_titanic


while True:
    print("\n_-_-_-_-_-_-_-_-_- Menu do Titanic _-_-_-_-_-_-_-_-_-")
    print("1 - Exibir cabeçalho")
    print("2 - Exibir 5 primeiros passageiros")
    print("3 - Listar todos os passageiros")
    print("4 - Total de passageiros")
    print("5 - Estatísticas de idade")
    print("6 - Estatísticas de tarifa")
    print("7 - Frequência por classe")
    print("8 - Taxa de sobrevivência")
    print("9 - Taxa por sexo")
    print("10 - Taxa por classe")
    print("11 - Média de familiares")
    print("12 - Tarifas por porto")
    print("13 - Dados faltantes")
    print("14 - Perfil etário por classe")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        visualizacao.exibir_cabecalho()

    elif opcao == "2":
        visualizacao.exibir_primeiros_passageiros()

    elif opcao == "3":
        visualizacao.exibir_todos_dados()

    elif opcao == "4":
        analise_titanic.exibir_total()

    elif opcao == "5":
        print(estatisticas_idade(dados))

    elif opcao == "6":
        print(estatisticas_fare(dados))

    elif opcao == "7":
        print(frequencia_coluna(dados, 2))

    elif opcao == "8":
        print(round(taxa_sobrevivencia_geral(dados), 2), "%")

    elif opcao == "9":
        print(taxa_por_sexo(dados))

    elif opcao == "10":
        print(taxa_por_classe(dados))

    elif opcao == "11":
        print(media_familiares(dados))

    elif opcao == "12":
        print(tarifas_por_porto(dados))

    elif opcao == "13":
        print(dados_faltantes(dados))

    elif opcao == "14":
        print(perfil_etario_por_classe(dados))

    elif opcao == "0":
        break

    else:
        print("Opção inválida.")
