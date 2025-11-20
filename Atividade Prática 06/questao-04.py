import requests

"""
Crie um programa que consulte a cotação atual de uma
moeda estrangeira em relação ao Real Brasileiro (BRL). O
usuário deve informar o código da moeda desejada (ex: USD,
EUR, GBP), e o programa deve exibir o valor atual, máximo e
mínimo da cotação, além da data e hora da última
atualização. Utilize a API da AwesomeAPI para obter os
dados de cotação.
"""

try:
    moeda = input("Digite o código da moeda (USD, EUR, GBP...). OBS: consulte na Awesome API para verificar as siglas compatíveis: ").upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    dados = requests.get(url).json()

    chave = (moeda + "BRL").upper()

    if chave not in dados:
        print("Moeda inválida ou não encontrada.")
    else:
        info = dados[chave]
        print("Moeda:", info["code"])
        print("Valor atual:", info["bid"])
        print("Máximo:", info["high"])
        print("Mínimo:", info["low"])
        print("Última atualização:", info["create_date"])

except Exception:
    print("Erro ao acessar a API AwesomeAPI.")
finally:
    print("Até a próxima execução! :D")
