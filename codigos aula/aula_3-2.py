#dicionários

#nome = {chave:valor}

#Obtendo chaves e valores

computador = {'CPU':'Intel', 'RAM':'16gb', 'HD': 'SSD 16gb'}

# métodos keys()
# print(computador.keys())

#método values()
# print(computador.values())

notas = {'Py': 5, 'Java': 7, 'BD' : 9}
lista_notas = list(notas.values())

# Percorrendo elesmentos no dicionário
# for chave in computador.keys():
#    print(f'Chave = {chave} e Valor = {computador[chave]}')
# for valor in notas.values():
#    print(f'Nota: {valor}')    

#método dict.items()
# lista = notas.items()
# lista = list(notas.items())
# for chave, valor in notas.items():
#   print(f'{chave}:{valor}')

# Adicionando elementos ao dicionários
#pessoa = {'nome':'Pedro'}
# pessoa['idade'] = 20
# print(pessoa)
# metodo update()
# pessoa.update({'nome':'matheus'})
# print (pessoa)

#metodo pop

lista_compras = {'maça':2, 'banana':10, 'farinha':2, 'Ovos':24}

ovos = lista_compras.pop('Ovos')
print(ovos)

#metodo popitem()
#produto = lsita_compras.popitem()
#