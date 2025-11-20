import random
import string

"""
Crie um programa que gera uma senha aleatória com o
módulo random, utilizando caracteres especiais,
possibilitando o usuário a informar a quantidade de
caracteres dessa senha aleatória.
"""

try:
    tamanhoDaSenha = int(input("Quantos caracteres terá a senha? "))

    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = "".join(random.choice(caracteres) for _ in range(tamanhoDaSenha))

    print("Senha gerada:", senha)

except ValueError:
    print("Erro: digite um número válido!")
finally:
    print("Até a próxima execução! :D")
