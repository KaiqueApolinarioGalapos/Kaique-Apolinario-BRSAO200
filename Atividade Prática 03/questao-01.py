"""
1- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

*Criança (0-12 anos),
*Adolescente (13-17 anos),
*Adulto (18-59 anos) ou
*Idoso (60 anos ou mais).
"""

idade = int(input("Qual sua idade? "))

if 0 <= idade <= 12:
    categoria = "'Buá, buá!' Você é uma criança."
elif 13 <= idade <= 17:
    categoria = "'Que saco, mãe!' Você é adolescente."
elif 18 <= idade <= 59:
    categoria = "'Sua ansiedade e depressão estão piorando.' Você é adulto(a)."
elif idade >= 60:
    categoria = "'Sua hora está chegando'. Você é idoso(a)."
else:
    categoria = "Idade inválida"

print(f"{categoria}")