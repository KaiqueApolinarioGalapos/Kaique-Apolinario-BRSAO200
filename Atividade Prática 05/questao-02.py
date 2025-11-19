"""
Crie uma função que verifique se uma palavra ou frase é um
palíndromo (lê-se igual de trás para frente, ignorando
espaços e pontuação).

Se o resultado é True, responda “Sim”, se o resultado for
False, responda “Não”
"""

def eh_palindromo(texto):
    texto_limpo = "".join(c.lower() for c in texto if c.isalnum())
    return texto_limpo == texto_limpo[::-1]


try:
    frase = input("Digite uma palavra ou frase: ")

    resultado = eh_palindromo(frase)

    print("Sim" if resultado else "Não")

except Exception:
    print("Ocorreu um erro inesperado!")

finally:
    print("Fim da verificação de palíndromo.\n")
