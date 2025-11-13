"""2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
"""

produto = "Camiseta"
preco = 50.00
porDeDesconto = 20 / 100
descSobrePreco = preco * porDeDesconto

print(f"Assumindo 20% de desconto sobre o preco de {preco} reais da {produto}, o valor final é {preco - descSobrePreco}.")