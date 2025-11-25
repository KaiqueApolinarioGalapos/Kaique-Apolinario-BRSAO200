"""
Crie um script em Python que escreva dados em um arquivo CSV. O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.
"""
import csv

try:
    nome = input("Nome: ")
    idade = int(input("Idade: ")) 
    cidade = input("Cidade: ")

    with open("pessoas.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([nome, idade, cidade])

    print("Dados colocados no arquivo pessoas.cvs!")

except ValueError:
    print("Idade inválida. Digite um número inteiro.")

except Exception as e:
    print("Ocorreu um erro:", e)
