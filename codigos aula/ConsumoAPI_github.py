import requests 

print('GitHub users')
username= input('Username: ')
url = f'https://api.github.com/users/{username}'

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(data)
    print(f'Nome Completo: {data["name"]}')
    print(f'Bio: {data["bio"]}')
    print(f'Localização: {data["location"]}')
    print(f'Seguidores: {data["followers"]}')
    print(f'Seguindo: {data["following"]}')
else:
    print('Usuário não encontrado!')

    