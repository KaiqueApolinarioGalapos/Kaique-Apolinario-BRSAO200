notas = []
print("Digite as notas dos alunos. Para encerrar, digite 'fim'.\n")

while True:
    entrada = input("Digite uma nota (0 a 10) ou 'fim': ").strip().lower()

    if entrada == 'fim':
        break

    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida! Digite apenas valores entre 0 e 10.")
    except ValueError:
        print("Entrada inválida! Digite um número ou 'fim'.")
    finally:
        print("Carregando próximo código ..........")

if len(notas) > 0:
    media = sum(notas) / len(notas)
    print(f"\nMédia da turma: {media:.2f}")
else:
    print("\nNenhuma nota válida foi registrada.")


