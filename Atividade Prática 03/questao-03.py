"""
3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""
temp = float(input("Temperatura: "))
origem = input("Converter de (Digite um desses 3: C/F/K): ")
convertido = input("Converter para (Digite um desses 3: C/F/K): ")

# Converter origem para Celsius
if origem == "C":
    c = temp
elif origem == "F":
    c = (temp - 32) * 5/9
elif origem == "K":
    c = temp - 273.15
else:
    print("Unidade de origem inválida!")

# Converter Celsius para destino
if convertido == "C":
    resultado = c
elif convertido == "F":
    resultado = c * 9/5 + 32
elif convertido == "K":
    resultado = c + 273.15
else:
    print("Unidade de destino inválida!")

print(f"Resultado: {resultado:.2f} {convertido}")



