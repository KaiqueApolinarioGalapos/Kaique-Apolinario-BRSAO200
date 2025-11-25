"""
Crie um script em Python que leia e escreva dados em um arquivo JSON. O arquivo JSON deve conter informações de uma pessoa, com campos nome, idade e cidade.
"""
import json

try:
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cidade = input("Cidade: ")

    pessoa = {
        "nome": nome,
        "idade": idade,
        "cidade": cidade
    }

except ValueError:
    print("Você não digitou uma idade válida. Tente novamente.")
    exit()

except Exception:
    print("Ocorreu um erro inesperado.")
    exit()

with open("pessoa.json", "w", encoding="utf-8") as arquivo:
    json.dump(pessoa, arquivo, indent=4, ensure_ascii=False)

print("Arquivo JSON criado! Agora vamos para a parte de ler o código:")

with open("pessoa.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

print("Nome:", dados["nome"])
print("Idade:", dados["idade"])
print("Cidade:", dados["cidade"])