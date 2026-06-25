#Funções para exibir os dados dos passageiros.

import importacao

arquivo = open("train.csv","r")

conteudo = arquivo.readlines()

linhas = 0 

for lines in conteudo:

    if linhas < 6:

        print(lines, end ="")

    linhas += 1

arquivo.close()