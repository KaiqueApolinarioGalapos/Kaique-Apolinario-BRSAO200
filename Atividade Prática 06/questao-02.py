import requests

"""
Crie um programa que gera um perfil de usuário aleatório usando a
API 'Random User Generator'. O programa deve exibir o nome, email
e país do usuário gerado."
"""

try:
    requisicao = requests.get("https://randomuser.me/api/").json()
    user = requisicao["results"][0]

    nome = f"{user['name']['first']} {user['name']['last']}"
    email = user["email"]
    pais = user["location"]["country"]

    print("Nome:", nome)
    print("Email:", email)
    print("País:", pais)

except Exception:
    print("Erro ao acessar a API Random User Generator.")
finally:
    print("Até a próxima execução! :D")
