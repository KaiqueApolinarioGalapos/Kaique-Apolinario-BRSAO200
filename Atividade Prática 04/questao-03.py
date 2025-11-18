pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro ou 'fim' para encerrar: ")

    if entrada.lower() == "fim":
        break

    try:
        numero = int(entrada)

        if numero % 2 == 0:
            print("O número é PAR.")
            pares += 1
        else:
            print("O número é ÍMPAR.")
            impares += 1

    except ValueError:
        print("Erro: Entrada inválida! Digite apenas números inteiros.\n")
    finally:
        print("Carregando próximo código ..........")

print(f"Total de números pares: {pares}")
print(f"Total de números ímpares: {impares}")
