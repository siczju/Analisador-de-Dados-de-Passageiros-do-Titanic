#Funções para carregar o arquivo CSV.

import os
import csv

def dados():

    if os.path.exists("train.csv"):
        arquivo_body = [ ]
        arquivo_title = [ ]

        arquivo = open("train.csv","r")

        listas = csv.reader(arquivo)

        for i in listas:
            arquivo_body.append(i)

        arquivo_title.append(arquivo_body[0])
        del arquivo_body[0]
        arquivo.close()

    print(arquivo_title,"\n")
    print(arquivo_body)

    return(arquivo_body,arquivo_title)

dados()