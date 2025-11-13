"""1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""

valorReais = 100.00
precoDolar = 5.20
precoEuro = 6.15

print(f'Os valores convertidos, arredondando para duas casas decimais: R$ {valorReais:.2f} é igual a {(valorReais/precoDolar):.2f} dólares e {(valorReais/precoEuro):.2f} euros.')