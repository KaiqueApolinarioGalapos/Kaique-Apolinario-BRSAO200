import requests
"""
Desenvolva um programa que consulte informações de
endereço a partir de um CEP fornecido pelo usuário,
utilizando a API ViaCEP. O programa deve exibir o
logradouro, bairro, cidade e estado correspondentes ao CEP
consultado.
"""

try:
    cep = input("Digite o CEP (somente números): ")

    requisicao = requests.get(f"https://viacep.com.br/ws/{cep}/json/").json()

    if "erro" in requisicao:
        print("CEP não encontrado.")
    else:
        print("Logradouro:", requisicao["logradouro"])
        print("Bairro:", requisicao["bairro"])
        print("Cidade:", requisicao["localidade"])
        print("Estado:", requisicao["uf"])

except Exception:
    print("Erro ao acessar a API ViaCEP.")
finally:
    print("Até a próxima execução! :D")