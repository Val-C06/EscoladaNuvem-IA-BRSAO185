""
# Crie um programa que gera um perfil de usuario aleatorio usando a API 'Random user Generator'
""

import requests

def obter_usuario_aleatorio():
    url = 'https://randomuser.me/api'

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()['results'][0]
        nome = dados['name']['first']
        email = dados['email']
        país = dados['location']['country']
        return f"\nNome: {nome}\nEmail: {email}\nPaís: {país}"
    except requests.RequestException as e:
        return f"Erro ao obter usuario aleatório{e}"
    
print("Gerando um usuário aleatorio: ")
usuario = obter_usuario_aleatorio()
print(usuario)

if __name__ == "__main__"

