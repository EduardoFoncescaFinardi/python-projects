import requests

cep = "04209000"

cep = cep.replace("-","")

if len(cep) == 8:
    link = f'https://viacep.com.br/ws/{cep}/json/'

    requisicao = requests.get(link)
    print(requisicao)

    dic_requisicao = requisicao.json()
    print(dic_requisicao)

    uf = dic_requisicao['uf']
    cidade = dic_requisicao['localidade']
    bairro = dic_requisicao['bairro']
    print(f'Cidade: {cidade}')
    print(f'Estado: {uf}')
    print(f'Bairro: {bairro}')
else:
    print('CEP inválido!')