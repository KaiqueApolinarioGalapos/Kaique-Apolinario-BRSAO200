"""
4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
"""

distancia = 300
combustivelGasto = 25

print(f"Considerando a distância percorrida de {distancia}km e {combustivelGasto} litros gastos. O consumo médio de litros por quilômetro é de {(distancia/combustivelGasto):.2f}km/l")