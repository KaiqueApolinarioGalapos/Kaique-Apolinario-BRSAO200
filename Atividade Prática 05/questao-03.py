"""
Crie um programa que serve para calcular o preço final de um produto após
aplicar um desconto percentual.

Cálculo de desconto: Calcula o valor do desconto baseado em uma
porcentagem.

Preço final: Determina o novo preço após o desconto.

Formatação: Arredonda o resultado para 2 casas decimais (centavos).

Interação com usuário: Pede os valores necessários e mostra o resultado
formatado.
"""

def calcular_preco_final(preco, desconto):
    valor_desconto = preco * (desconto / 100)
    preco_final = preco - valor_desconto
    return round(preco_final, 2)

try:
    preco = float(input("Digite o preço do produto: R$ "))
    desconto = float(input("Digite o percentual de desconto (%): "))

    preco_final = calcular_preco_final(preco, desconto)

    print(f"Preço final após desconto: R$ {preco_final:.2f}")

except ValueError:
    print("Erro: digite apenas números válidos!")
