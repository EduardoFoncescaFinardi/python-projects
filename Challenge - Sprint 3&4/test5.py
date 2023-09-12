# Dicionário com uma lista
meu_dicionario = {
    'nomes': ['Alice', 'Bob', 'Carol', 'David'],
    'idades': [25, 30, 35, 40]
}

# Acessando a lista 'nomes' no dicionário
lista_nomes = meu_dicionario['nomes']

# Modificando a lista 'nomes'
lista_nomes[1] = 'Bobby'
lista_nomes.append('Eva')

# Atualizando o valor associado à chave 'nomes' no dicionário
meu_dicionario['nomes'] = lista_nomes

# Imprimindo o dicionário atualizado
print(meu_dicionario)
