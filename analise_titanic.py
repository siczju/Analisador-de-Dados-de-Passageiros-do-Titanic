import importacao

arquivo_body, arquivo_title = importacao.dados()

def exibir_total():
    print(f"O total de passageiros listados é: {len(arquivo_body)}")

def estatisticas_idade():
    i = 0
    quantidade_idades = 0
    soma = 0.0
    menorIdade = None
    maiorIdade = None

    while(i < len(arquivo_body)):
        if arquivo_body[i][5] != '':
            idade = float(arquivo_body[i][5])
            quantidade_idades += 1
            soma += idade

            if menorIdade == None or menorIdade >= idade:
                menorIdade = idade
            if maiorIdade == None or maiorIdade <= idade:
                maiorIdade = idade

        i += 1
        
    if quantidade_idades == 0:
        print("Não há idades válidas para calcular as estatísticas.")
        return
    
    print(f"A média de todas idades é: {soma / quantidade_idades:.2f}")
    print(f"A maior idade é: {maiorIdade:.2f}")
    print(f"A menor idade é: {menorIdade:.2f}")
