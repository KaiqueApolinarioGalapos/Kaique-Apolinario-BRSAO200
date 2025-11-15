"""
2- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"
"""

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso. Partiu cuidar da saúde!"
elif imc < 25:
    classificacao = "Peso normal. Cuidado para não perder o controle."
elif imc < 30:
    classificacao = "Sobrepeso. Não é algo extremamente preocupante, mas fica o alerta."
else:
    classificacao = "Obeso. Cuidado redobrado a longo prazo."

print(f"Seu IMC é {imc:.2f} — {classificacao}")