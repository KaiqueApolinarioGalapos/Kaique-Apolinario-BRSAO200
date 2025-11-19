from datetime import datetime

"""
Crie uma função que calcule a idade de uma pessoa em dias,
baseada no ano de nascimento.
"""

def idade_em_dias(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade * 365
try:
    ano = int(input("Digite seu ano de nascimento: "))
    print(f"Você tem {idade_em_dias(ano)} dias de idade.")
except ValueError:
    print("Erro: Ops. Ano inválido.")
