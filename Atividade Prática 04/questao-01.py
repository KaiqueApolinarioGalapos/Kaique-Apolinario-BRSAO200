while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Errado: você deve digitar apenas números!\n")
        continue
    finally:
        print("Carregando próximo código ..........")

    try:
        operacao = input("Digite a operação (+, -, *, /): ").strip()
        if operacao not in ["+", "-", "*", "/"]:
            raise Exception("Operação inválida.")
    except Exception as e:
        print(f"Errado: {e}\n")
        continue
    finally:
        print("Carregando próximo código ..........")

    try:
        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            resultado = num1 / num2
    except ZeroDivisionError:
        print("Errado: divisão por zero não é permitida!\n")
        continue
    finally:
        print("Carregando próximo código ..........")

    print(f"Resultado: {resultado}")
    break
