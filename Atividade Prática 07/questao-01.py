"""
Leia um arquivo que contém dados de log de treinamento de
modelos de Machine Learning. Calcule a média e o desvio
padrão do tempo de execução constantes.
"""

import pandas as pd

try:
    df = pd.read_csv("./Atividade Prática 07/log_treinamento.csv")

    if "tempo" not in df.columns:
        raise ValueError("A coluna 'tempo' não foi encontrada no arquivo CSV.")

    media = df["tempo"].mean()
    desvio = df["tempo"].std()

    print("Média do tempo de execução:", media)
    print("Desvio padrão do tempo de execução:", desvio)

except FileNotFoundError:
    print("Erro: O arquivo 'log_treinamento.txt' não foi encontrado.")

except ValueError as e:
    print("Erro no formato do arquivo:", e)

except Exception as e:
    print("Ocorreu um erro inesperado:", e)
