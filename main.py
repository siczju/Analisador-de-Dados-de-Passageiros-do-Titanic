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
        analise_titanic.estatisticas_idade()

    elif opcao == "6":
        analise_titanic.estatisticas_fare()

    elif opcao == "7":
        analise_titanic.frequencia_coluna()

    elif opcao == "8":
        analise_titanic.taxa_sobrevivencia_geral()

    elif opcao == "9":
        analise_titanic.taxa_por_sexo()

    elif opcao == "10":
        analise_titanic.taxa_por_classe()

    elif opcao == "11":
        analise_titanic.media_familiares()

    elif opcao == "12":
        analise_titanic.tarifas_por_porto()

    elif opcao == "13":
        analise_titanic.dados_faltantes()

    elif opcao == "14":
        analise_titanic.perfil_etario_por_classe()

    elif opcao == "0":
        break

    else:
        print("Opção inválida.")
