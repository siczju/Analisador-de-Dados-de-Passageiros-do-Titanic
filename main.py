import importacao
import visualizacao
import analise_titanic


def main():
    """
    Ponto de entrada do programa: exibe o menu e trata a escolha do usuário.

    Parâmetros:
    - nenhum.

    Retorno:
    - None: carrega os dados e fica em loop executando a opção escolhida até
      o usuário digitar 0 para sair.
    """
    # Carrega os dados uma única vez e repassa para as funções como argumento.
    arquivo_body, arquivo_title = importacao.dados()

    while True:
        print("\n_-_-_-_-_-_-_-_-_- Menu do Titanic _-_-_-_-_-_-_-_-_-")
        print("1 - Exibir cabeçalho")
        print("2 - Exibir 5 primeiros passageiros")
        print("3 - Listar todos os passageiros")
        print("4 - Total de passageiros")
        print("5 - Estatísticas de idade")
        print("6 - Estatísticas de tarifa por porto")
        print("7 - Frequência por classe")
        print("8 - Taxa de sobrevivência")
        print("9 - Taxa por sexo")
        print("10 - Taxa por classe")
        print("11 - Média de familiares")
        print("12 - Tarifas por porto")
        print("13 - Dados faltantes")
        print("14 - Perfil etário por classe")
        print("15 - Estatísticas de tarifa (mínima, máxima e média)")
        print("0 - Sair")

        opcao = input("Escolha: ")

         if opcao == "1":
            print("\n")
            print("_________________________Cabeçalho__________________________\n")
            visualizacao.exibir_cabecalho(arquivo_title)

        elif opcao == "2":
            print("\n")
            print("_________________________Cinco Primeiros Passageiros__________________________\n")
            visualizacao.exibir_primeiros_passageiros(arquivo_body)

        elif opcao == "3":
            print("\n")
            print("_________________________Lista de Todos os passageiros__________________________\n")
            visualizacao.exibir_todos_dados(arquivo_body, arquivo_title)

        elif opcao == "4":
            print("_________________________Total de Passageiros__________________________")
            analise_titanic.exibir_total(arquivo_body)

        elif opcao == "5":
            analise_titanic.estatisticas_idade(arquivo_body)

        elif opcao == "6":
            analise_titanic.estatisticas_fare(arquivo_body)

        elif opcao == "7":
            analise_titanic.frequencia_coluna(arquivo_body)

        elif opcao == "8":
            analise_titanic.taxa_sobrevivencia_geral(arquivo_body)

        elif opcao == "9":
            analise_titanic.taxa_por_sexo(arquivo_body)

        elif opcao == "10":
            analise_titanic.taxa_por_classe(arquivo_body)

        elif opcao == "11":
            analise_titanic.media_familiares(arquivo_body)

        elif opcao == "12":
            analise_titanic.tarifas_por_porto(arquivo_body)

        elif opcao == "13":
            analise_titanic.dados_faltantes(arquivo_body)

        elif opcao == "14":
            analise_titanic.perfil_etario_por_classe(arquivo_body)

        elif opcao == "15":
            analise_titanic.estatisticas_tarifa(arquivo_body)

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
