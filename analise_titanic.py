def exibir_total(arquivo_body):
    """
    Conta e exibe o total de passageiros listados na base.

    Parâmetros:
    - arquivo_body (list): Lista de listas contendo os dados do Titanic.

    Retorno:
    - None: exibe na tela o total de passageiros.
    """
    print(f"O total de passageiros listados é: {len(arquivo_body)}")

def estatisticas_idade(arquivo_body):
    """
    Calcula a idade média, máxima e mínima dos passageiros (coluna Age).

    Parâmetros:
    - arquivo_body (list): Lista de listas contendo os dados do Titanic.

    Retorno:
    - None: exibe na tela a média, a maior e a menor idade.
    """
    i = 0
    quantidade_idades = 0
    soma = 0.0
    menorIdade = None
    maiorIdade = None

    while(i < len(arquivo_body)):
        if arquivo_body[i][5] != '':
            try:
                idade = float(arquivo_body[i][5])
            except ValueError:
                i += 1
                continue

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

def estatisticas_tarifa(arquivo_body):
    """
    Calcula a tarifa média, máxima e mínima dos passageiros (coluna Fare).

    Parâmetros:
    - arquivo_body (list): Lista de listas contendo os dados do Titanic.

    Retorno:
    - None: exibe na tela a média, a maior e a menor tarifa.
    """
    i = 0
    quantidade_tarifas = 0
    soma = 0.0
    menorTarifa = None
    maiorTarifa = None

    while(i < len(arquivo_body)):
        if arquivo_body[i][9] != '':
            try:
                tarifa = float(arquivo_body[i][9])
            except ValueError:
                i += 1
                continue

            quantidade_tarifas += 1
            soma += tarifa

            if menorTarifa == None or menorTarifa >= tarifa:
                menorTarifa = tarifa
            if maiorTarifa == None or maiorTarifa <= tarifa:
                maiorTarifa = tarifa

        i += 1

    if quantidade_tarifas == 0:
        print("Não há tarifas válidas para calcular as estatísticas.")
        return

    print(f"A média de todas as tarifas é: {soma / quantidade_tarifas:.2f}")
    print(f"A maior tarifa é: {maiorTarifa:.2f}")
    print(f"A menor tarifa é: {menorTarifa:.2f}")

def frequencia_coluna(arquivo_body):
    """
    Conta a frequência dos valores de uma coluna escolhida pelo usuário.

    Parâmetros:
    - arquivo_body (list): Lista de listas contendo os dados do Titanic.

    Retorno:
    - None: exibe na tela a contagem de cada categoria da coluna escolhida
      (Pclass, Sex, Embarked ou Survived).
    """
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

def taxa_sobrevivencia_geral(arquivo_body):
        """
        Calcula a taxa de sobrevivência geral, por sexo e por classe.

        Parâmetros:
        - arquivo_body (list): Lista de listas contendo os dados do Titanic.

        Retorno:
        - None: exibe na tela a porcentagem geral de sobreviventes e as taxas
          separadas por sexo (male/female) e por classe (1ª, 2ª e 3ª).
        """
        i = 0
        contadorDe0 = 0
        contadorDe1 = 0
        contadorDeF = 0
        contadorDeM = 0
        contadorDe0F = 0
        contadorDe0M = 0
        contadorClasse1 = 0
        contadorClasse2 = 0
        contadorClasse3 = 0
        contadorMorteClasse1 = 0
        contadorMorteClasse2 = 0
        contadorMorteClasse3 = 0

        while i < len(arquivo_body):
            if arquivo_body[i][1] != '' and arquivo_body[i][4] != '' and arquivo_body[i][2] != '':
                try:
                    Survived = int(arquivo_body[i][1])
                    Sex = arquivo_body[i][4].strip().lower()
                    Pclass = int(arquivo_body[i][2])
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

                if Pclass == 1:
                    contadorClasse1 += 1
                    if Survived == 0:
                        contadorMorteClasse1 += 1
                elif Pclass == 2:
                    contadorClasse2 += 1
                    if Survived == 0:
                        contadorMorteClasse2 += 1
                elif Pclass == 3:
                    contadorClasse3 += 1
                    if Survived == 0:
                        contadorMorteClasse3 += 1

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

        if contadorClasse1 > 0:
            print(f"\n A taxa de sobrevivência da 1ª classe é: {((contadorClasse1 - contadorMorteClasse1) / contadorClasse1) * 100:.2f}%")
        else:
            print("\n A taxa de sobrevivência da 1ª classe é: sem dados")

        if contadorClasse2 > 0:
            print(f"\n A taxa de sobrevivência da 2ª classe é: {((contadorClasse2 - contadorMorteClasse2) / contadorClasse2) * 100:.2f}%")
        else:
            print("\n A taxa de sobrevivência da 2ª classe é: sem dados")

        if contadorClasse3 > 0:
            print(f"\n A taxa de sobrevivência da 3ª classe é: {((contadorClasse3 - contadorMorteClasse3) / contadorClasse3) * 100:.2f}%")
        else:
            print("\n A taxa de sobrevivência da 3ª classe é: sem dados")
        print(f"")
    
def estatisticas_fare(arquivo_body):
    """
    Soma as tarifas arrecadadas por porto de embarque e calcula a média.

    Parâmetros:
    - arquivo_body (list): Lista de listas contendo os dados do Titanic.

    Retorno:
    - None: exibe na tela o total e a média de tarifas de cada porto (C, Q, S)
      e qual deles teve a maior e a menor arrecadação.
    """
    quantidade_tarifas_c = 0
    quantidade_tarifas_q = 0
    quantidade_tarifas_s = 0
    tarifas_c = 0
    tarifas_q = 0
    tarifas_s = 0
    
    for i in range(len(arquivo_body)):
        try:
            tarifa = float(arquivo_body[i][9]) if arquivo_body[i][9] != '' else 0
        except ValueError:
            tarifa = 0

        if arquivo_body[i][11] == 'C':
            quantidade_tarifas_c += 1
            tarifas_c += tarifa
        elif arquivo_body[i][11] == 'Q':
            quantidade_tarifas_q += 1
            tarifas_q += tarifa
        elif arquivo_body[i][11] == 'S':
            quantidade_tarifas_s += 1
            tarifas_s += tarifa


    if tarifas_c > tarifas_q and tarifas_q > tarifas_s:
        print("O setor com a maior tarifa foi o C, e o com a menor foi o S")

    elif tarifas_c > tarifas_s and tarifas_s > tarifas_q:
        print("O setor com a maior tarifa foi o C, e o com a menor foi o Q")

    elif tarifas_q > tarifas_c and tarifas_c > tarifas_s:
        print("O setor com a maior tarifa foi o Q, e o com a menor foi o S")

    elif tarifas_q > tarifas_s and tarifas_s > tarifas_c:
        print("O setor com a maior tarifa foi o Q, e o com a menor foi o C")

    elif tarifas_s > tarifas_c and tarifas_c > tarifas_q:
        print("O setor com a maior tarifa foi o S, e o com a menor foi o Q")

    elif tarifas_s > tarifas_q and tarifas_q > tarifas_c:
        print("O setor com a maior tarifa foi o S, e o com a menor foi o C")
    

    print(f"Tarifas C: {quantidade_tarifas_c}, Total: {tarifas_c}")
    print(f"Tarifas Q: {quantidade_tarifas_q}, Total: {tarifas_q}")
    print(f"Tarifas S: {quantidade_tarifas_s}, Total: {tarifas_s}")
    print(f"Média de tarifas C: {tarifas_c / quantidade_tarifas_c if quantidade_tarifas_c > 0 else 0:.2f}")
    print(f"Média de tarifas Q: {tarifas_q / quantidade_tarifas_q if quantidade_tarifas_q > 0 else 0:.2f}")
    print(f"Média de tarifas S: {tarifas_s / quantidade_tarifas_s if quantidade_tarifas_s > 0 else 0:.2f}")

def dados_faltantes(arquivo_body):
    """
    Contabiliza os dados faltantes de idade (Age) e cabine (Cabin).

    Parâmetros:
    - arquivo_body (list): Lista de listas contendo os dados do Titanic.

    Retorno:
    - None: exibe na tela quantos registros de Age estão vazios e a
      porcentagem de passageiros sem informação de Cabin.
    """
    if len(arquivo_body) == 0:
        print("Não há dados carregados para analisar.")
        return

    age_vazio = 0
    cabin_vazio = 0

    for i in range(len(arquivo_body)):
        if arquivo_body[i][5] == "":
            age_vazio += 1

        if arquivo_body[i][10] == "":
            cabin_vazio += 1

    print(f"A quantidade de registros AGE vazios na documentação é: {age_vazio}")
    print(f"A porcentagem de passageiros sem registro de CABIN é {cabin_vazio / len(arquivo_body) * 100:.2f}%")

def taxa_por_sexo(arquivo_body):
    """
    Calcula a taxa de sobrevivência separada por sexo (male/female).

    Parâmetros:
    - arquivo_body (list): Lista de listas contendo os dados do Titanic.

    Retorno:
    - None: exibe na tela a porcentagem de sobreviventes de cada sexo.
    """
    total_f = 0
    total_m = 0
    sobreviventes_f = 0
    sobreviventes_m = 0

    for i in range(len(arquivo_body)):
        if arquivo_body[i][1] != '' and arquivo_body[i][4] != '':
            try:
                survived = int(arquivo_body[i][1])
            except ValueError:
                continue

            sexo = arquivo_body[i][4].strip().lower()

            if sexo == 'female':
                total_f += 1
                if survived == 1:
                    sobreviventes_f += 1
            elif sexo == 'male':
                total_m += 1
                if survived == 1:
                    sobreviventes_m += 1

    if total_f > 0:
        print(f"Taxa de sobrevivência (female): {sobreviventes_f / total_f * 100:.2f}%")
    else:
        print("Taxa de sobrevivência (female): sem dados")

    if total_m > 0:
        print(f"Taxa de sobrevivência (male): {sobreviventes_m / total_m * 100:.2f}%")
    else:
        print("Taxa de sobrevivência (male): sem dados")

def taxa_por_classe(arquivo_body):
    """
    Calcula a taxa de sobrevivência separada por classe (1ª, 2ª e 3ª).

    Parâmetros:
    - arquivo_body (list): Lista de listas contendo os dados do Titanic.

    Retorno:
    - None: exibe na tela a porcentagem de sobreviventes de cada classe.
    """
    total_classe1 = 0
    total_classe2 = 0
    total_classe3 = 0
    sobreviventes_classe1 = 0
    sobreviventes_classe2 = 0
    sobreviventes_classe3 = 0

    for i in range(len(arquivo_body)):
        if arquivo_body[i][1] != '' and arquivo_body[i][2] != '':
            try:
                survived = int(arquivo_body[i][1])
                pclass = int(arquivo_body[i][2])
            except ValueError:
                continue

            if pclass == 1:
                total_classe1 += 1
                if survived == 1:
                    sobreviventes_classe1 += 1
            elif pclass == 2:
                total_classe2 += 1
                if survived == 1:
                    sobreviventes_classe2 += 1
            elif pclass == 3:
                total_classe3 += 1
                if survived == 1:
                    sobreviventes_classe3 += 1

    if total_classe1 > 0:
        print(f"Taxa de sobrevivência da 1ª classe: {sobreviventes_classe1 / total_classe1 * 100:.2f}%")
    else:
        print("Taxa de sobrevivência da 1ª classe: sem dados")

    if total_classe2 > 0:
        print(f"Taxa de sobrevivência da 2ª classe: {sobreviventes_classe2 / total_classe2 * 100:.2f}%")
    else:
        print("Taxa de sobrevivência da 2ª classe: sem dados")

    if total_classe3 > 0:
        print(f"Taxa de sobrevivência da 3ª classe: {sobreviventes_classe3 / total_classe3 * 100:.2f}%")
    else:
        print("Taxa de sobrevivência da 3ª classe: sem dados")

def media_familiares(arquivo_body):
    """
    Analisa a composição familiar somando SibSp e Parch de cada passageiro.

    Parâmetros:
    - arquivo_body (list): Lista de listas contendo os dados do Titanic.

    Retorno:
    - None: exibe na tela quantos viajavam sozinhos, quantos em grupo e a
      média de familiares a bordo.
    """
    total_passageiros = 0
    soma_familiares = 0
    sozinhos = 0
    em_grupo = 0

    for i in range(len(arquivo_body)):
        if arquivo_body[i][6] != '' and arquivo_body[i][7] != '':
            try:
                sibsp = int(arquivo_body[i][6])
                parch = int(arquivo_body[i][7])
            except ValueError:
                continue

            tamanho_familia = sibsp + parch
            total_passageiros += 1
            soma_familiares += tamanho_familia

            if tamanho_familia == 0:
                sozinhos += 1
            else:
                em_grupo += 1

    if total_passageiros == 0:
        print("Não há dados válidos para analisar a composição familiar.")
        return

    print(f"Passageiros que viajavam sozinhos: {sozinhos}")
    print(f"Passageiros que viajavam em grupo: {em_grupo}")
    print(f"Média de familiares a bordo: {soma_familiares / total_passageiros:.2f}")

def tarifas_por_porto(arquivo_body):
    """
    Calcula a tarifa média de cada porto de embarque (Embarked x Fare).

    Parâmetros:
    - arquivo_body (list): Lista de listas contendo os dados do Titanic.

    Retorno:
    - None: exibe na tela a tarifa média de cada porto (C, Q, S) e indica qual
      teve a tarifa mais cara e qual teve a mais barata.
    """
    quantidade_c = 0
    quantidade_q = 0
    quantidade_s = 0
    soma_c = 0.0
    soma_q = 0.0
    soma_s = 0.0

    for i in range(len(arquivo_body)):
        if arquivo_body[i][9] != '':
            try:
                fare = float(arquivo_body[i][9])
            except ValueError:
                continue

            porto = arquivo_body[i][11].strip().upper()

            if porto == 'C':
                soma_c += fare
                quantidade_c += 1
            elif porto == 'Q':
                soma_q += fare
                quantidade_q += 1
            elif porto == 'S':
                soma_s += fare
                quantidade_s += 1

    if quantidade_c > 0:
        media_c = soma_c / quantidade_c
        print(f"Tarifa média em C: {media_c:.2f}")
    else:
        media_c = 0
        print("Tarifa média em C: sem dados")

    if quantidade_q > 0:
        media_q = soma_q / quantidade_q
        print(f"Tarifa média em Q: {media_q:.2f}")
    else:
        media_q = 0
        print("Tarifa média em Q: sem dados")

    if quantidade_s > 0:
        media_s = soma_s / quantidade_s
        print(f"Tarifa média em S: {media_s:.2f}")
    else:
        media_s = 0
        print("Tarifa média em S: sem dados")

    # Descobre qual porto teve a maior tarifa média
    if media_c >= media_q and media_c >= media_s:
        print(f"\nPorto com a tarifa média mais cara: C - {media_c:.2f}")
    elif media_q >= media_c and media_q >= media_s:
        print(f"\nPorto com a tarifa média mais cara: Q - {media_q:.2f}")
    else:
        print(f"\nPorto com a tarifa média mais cara: S - {media_s:.2f}")

    # Descobre qual porto teve a menor tarifa média
    if media_c <= media_q and media_c <= media_s:
        print(f"Porto com a tarifa média mais barata: C - {media_c:.2f}")
    elif media_q <= media_c and media_q <= media_s:
        print(f"Porto com a tarifa média mais barata: Q - {media_q:.2f}")
    else:
        print(f"Porto com a tarifa média mais barata: S - {media_s:.2f}")

def perfil_etario_por_classe(arquivo_body):
    """
    Calcula a idade média, mínima e máxima de cada classe (Pclass).

    Parâmetros:
    - arquivo_body (list): Lista de listas contendo os dados do Titanic.

    Retorno:
    - None: exibe na tela o perfil etário (média, mínima e máxima) de cada
      uma das três classes.
    """
    contador_classe1 = 0
    contador_classe2 = 0
    contador_classe3 = 0
    soma_classe1 = 0.0
    soma_classe2 = 0.0
    soma_classe3 = 0.0
    menor_classe1 = None
    menor_classe2 = None
    menor_classe3 = None
    maior_classe1 = None
    maior_classe2 = None
    maior_classe3 = None

    for i in range(len(arquivo_body)):
        if arquivo_body[i][2] != '' and arquivo_body[i][5] != '':
            try:
                pclass = int(arquivo_body[i][2])
                age = float(arquivo_body[i][5])
            except ValueError:
                continue

            if pclass == 1:
                contador_classe1 += 1
                soma_classe1 += age
                if menor_classe1 == None or age < menor_classe1:
                    menor_classe1 = age
                if maior_classe1 == None or age > maior_classe1:
                    maior_classe1 = age
            elif pclass == 2:
                contador_classe2 += 1
                soma_classe2 += age
                if menor_classe2 == None or age < menor_classe2:
                    menor_classe2 = age
                if maior_classe2 == None or age > maior_classe2:
                    maior_classe2 = age
            elif pclass == 3:
                contador_classe3 += 1
                soma_classe3 += age
                if menor_classe3 == None or age < menor_classe3:
                    menor_classe3 = age
                if maior_classe3 == None or age > maior_classe3:
                    maior_classe3 = age

    print("\n__________1ª Classe__________")
    if contador_classe1 > 0:
        print(f"Idade média: {soma_classe1 / contador_classe1:.2f}")
        print(f"Idade mínima: {menor_classe1:.2f}")
        print(f"Idade máxima: {maior_classe1:.2f}")
    else:
        print("Sem dados de idade para esta classe.")

    print("\n__________2ª Classe__________")
    if contador_classe2 > 0:
        print(f"Idade média: {soma_classe2 / contador_classe2:.2f}")
        print(f"Idade mínima: {menor_classe2:.2f}")
        print(f"Idade máxima: {maior_classe2:.2f}")
    else:
        print("Sem dados de idade para esta classe.")

    print("\n__________3ª Classe__________")
    if contador_classe3 > 0:
        print(f"Idade média: {soma_classe3 / contador_classe3:.2f}")
        print(f"Idade mínima: {menor_classe3:.2f}")
        print(f"Idade máxima: {maior_classe3:.2f}")
    else:
        print("Sem dados de idade para esta classe.")
