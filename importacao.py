#Funções para carregar o arquivo CSV.

import os
import csv

def dados():

    if os.path.exists("train.csv"):

        with open("train.csv", "r", encoding='utf-8', newline='') as arquivo:
            listas = csv.reader(arquivo)
            matriz = []
            for linha in listas:
                matriz.append(linha)

            arquivo_body = matriz
            arquivo_title = arquivo_body[0]
            del arquivo_body[0]

    return(arquivo_body, arquivo_title)
