# Analisador de Dados do Titanic

Este projeto tem como objetivo analisar os dados dos passageiros do Titanic a partir do arquivo `train.csv`. O sistema foi desenvolvido em Python utilizando programação modular, dividindo as funcionalidades em diferentes arquivos para facilitar a organização e manutenção do código.

## Estrutura do Projeto

* `main.py` - Controle do menu e interação com o usuário.
* `importacao.py` - Importação e carregamento dos dados.
* `visualizacao.py` - Exibição dos dados dos passageiros.
* `analise_titanic.py` - Funções de análise estatística.

## Funcionalidades

O sistema permite:

* Carregar os dados do arquivo CSV.
* Exibir o cabeçalho e os registros dos passageiros.
* Mostrar a quantidade total de passageiros.
* Calcular idade mínima, máxima e média.
* Calcular estatísticas das tarifas das passagens.
* Analisar frequências de categorias como classe e porto de embarque.
* Calcular taxas de sobrevivência gerais e por grupo.
* Analisar composição familiar dos passageiros.
* Identificar dados faltantes.
* Gerar estatísticas de idade por classe social.

## Dataset

Os dados utilizados neste projeto são da base Titanic, disponível no Kaggle:

https://www.kaggle.com/competitions/titanic/data

## Como Executar

1. Coloque o arquivo `train.csv` na pasta do projeto.
2. Execute o arquivo principal:

```bash
python main.py
```

## Integrantes

* Ana B.
* Júlio César
* João Vitor
* Isaac

## Observações

Todas as funções foram documentadas utilizando docstrings e o programa possui tratamento de exceções para situações como arquivo inexistente ou erros de leitura.
