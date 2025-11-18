while True:
    try:
        senha = input("Digite uma senha (ou 'sair' para encerrar): ")

        if senha.lower() == "sair":
            print("Programa encerrado.")
            break

        if len(senha) < 8:
            raise ValueError("A senha deve ter pelo menos 8 caracteres.")

        if not any(char.isdigit() for char in senha): #Aqui, cada caractere é lido um por um para verificar se há número
            raise ValueError("A senha deve conter pelo menos um número.")

        print("Senha forte! Acesso permitido. Bem vindoo!")
        break

    except ValueError as erro:
        print(f"Erro: {erro}\n")

    except Exception:
        print("Ocorreu um erro inesperado. Tente novamente.\n")

    finally:
        print("Tentativa finalizada. Próxima execução: \n")