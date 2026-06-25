import importacao

arquivo_body, arquivo_title = importacao.dados()

def exibir_total():
    print(f"O total de passageiros listados é: {len(arquivo_body)}")

