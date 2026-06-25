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

def frequencia_coluna():
    i = 0

    try:
        choose = int(input("\n Você quer ver a frequência de qual coluna:" \
                            "\n  1 - Pclass" \
                            "\n  2 - Sex" \
                            "\n  3 - Embarked" \
                            "\n  4 - Survived" \
                            "\nEscolha: "))
    except ValueError:
        print("Opção inválida. Digite um número entre 1 e 4.")
        return

    if choose < 1 or choose > 4:
        print("Opção inválida. Escolha uma opção entre 1 e 4.")
        return

    if choose == 1:
    # Contador de Pclass(1,2,3)
        contadorDe1 = 0
        contadorDe2 = 0
        contadorDe3 = 0

        while i < len(arquivo_body):
            if arquivo_body[i][2] != '':
                try:
                    Pclass = int(arquivo_body[i][2])
                except ValueError:
                    i += 1
                    continue

                if(Pclass == 1):
                    contadorDe1 += 1
                elif(Pclass == 2):
                    contadorDe2 += 1
                elif(Pclass == 3):
                    contadorDe3 += 1

            i += 1

        print(f"Pclass 1: {contadorDe1} passageiros")
        print(f"Pclass 2: {contadorDe2} passageiros")
        print(f"Pclass 3: {contadorDe3} passageiros")

    elif choose == 2:
    # Contador de sexos (F,M)
        contadorDeF = 0
        contadorDeM = 0

        while i < len(arquivo_body):
            if arquivo_body[i][4] != '':
                Sex = arquivo_body[i][4].strip().lower()

                if Sex == 'female':
                    contadorDeF += 1
                elif Sex == 'male':
                    contadorDeM += 1

            i += 1

        print(f"Male: {contadorDeM}")
        print(f"Female: {contadorDeF}")

    elif choose == 3:
        # Contador de embarked (C,Q,S)

        contadorDeC = 0
        contadorDeQ = 0
        contadorDeS = 0

        while i < len(arquivo_body):
            if arquivo_body[i][11] != '':
                embarked = arquivo_body[i][11].strip().upper()

                if embarked == 'C':
                    contadorDeC += 1
                elif embarked == 'Q':
                    contadorDeQ += 1
                elif embarked == 'S':
                    contadorDeS += 1

            i += 1

        print(f"Embarked C: {contadorDeC}")
        print(f"Embarked Q: {contadorDeQ}")
        print(f"Embarked S: {contadorDeS}")

    elif choose == 4:
        # Contador de survived (0,1)

        contadorDe0 = 0
        contadorDe1 = 0

        while i < len(arquivo_body):
            if arquivo_body[i][1] != '':
                try:
                    Survived = int(arquivo_body[i][1])
                except ValueError:
                    i += 1
                    continue

                if(Survived == 0):
                    contadorDe0 += 1
                elif(Survived == 1):
                    contadorDe1 += 1

            i += 1

        print(f"Survived 0: {contadorDe0}")
        print(f"Survived 1: {contadorDe1}")

def taxa_sobrevivencia_geral():
        i = 0
        contadorDe0 = 0
        contadorDe1 = 0
        contadorDeF = 0
        contadorDeM = 0
        contadorDe0F = 0
        contadorDe0M = 0

        while i < len(arquivo_body):
            if arquivo_body[i][1] != '' and arquivo_body[i][4] != '':
                try:
                    Survived = int(arquivo_body[i][1])
                    Sex = arquivo_body[i][4].strip().lower()
                except ValueError:
                    i += 1
                    continue

                if(Survived == 0):
                    contadorDe0 += 1
                elif(Survived == 1):
                    contadorDe1 += 1

                if Sex == 'female':
                    contadorDeF += 1
                elif Sex == 'male':
                    contadorDeM += 1
                    
                if(Survived == 0 and Sex == 'female'):
                    contadorDe0F += 1
                elif(Survived == 0 and Sex == 'male'):
                    contadorDe0M += 1

            i += 1

        if (contadorDe0 + contadorDe1) == 0:
            print("\n Não há dados válidos para calcular a taxa geral.")
            return

        print(f"\n A Porcentagem total de sobreviventes em relação ao total de passageiros é: {(contadorDe1 / (contadorDe0 + contadorDe1)) * 100:.2f}%")

        if contadorDeF > 0:
            print(f"\n A taxa de sobrevivência da mulher é: {((contadorDeF - contadorDe0F) / contadorDeF) * 100:.2f}%")
        else:
            print("\n A taxa de sobrevivência da mulher é: sem dados")

        if contadorDeM > 0:
            print(f"\n A taxa de sobrevivência do homem é: {((contadorDeM - contadorDe0M) / contadorDeM) * 100:.2f}%")
        else:
            print("\n A taxa de sobrevivência do homem é: sem dados")
        print(f"")