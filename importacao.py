#Funções para carregar o arquivo CSV.

import os
import csv

def dados():
    """
    Carrega o arquivo train.csv e separa o cabeçalho dos dados.

    Parâmetros:
    - nenhum: o arquivo lido é sempre o 'train.csv' do diretório atual.

    Retorno:
    - tuple (list, list): a matriz com os dados dos passageiros e a lista com
      os nomes das colunas. Devolve duas listas vazias se o arquivo não existir,
      estiver vazio ou não puder ser lido.
    """
    if not os.path.exists("train.csv"):
        print("Erro: o arquivo 'train.csv' não foi encontrado.")
        return [], []

    try:
        with open("train.csv", "r", encoding='utf-8', newline='') as arquivo:
            listas = csv.reader(arquivo)
            matriz = []
            for linha in listas:
                matriz.append(linha)
    except (OSError, csv.Error) as erro:
        print(f"Erro ao ler o arquivo 'train.csv': {erro}")
        return [], []

    if len(matriz) == 0:
        print("Aviso: o arquivo 'train.csv' está vazio.")
        return [], []

    arquivo_title = matriz[0]
    del matriz[0]
    arquivo_body = matriz

    return arquivo_body, arquivo_title
