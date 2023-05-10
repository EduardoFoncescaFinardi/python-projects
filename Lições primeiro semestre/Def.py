#manipulação de Listas com Funções
'''
1) Função tamanho _lista()
2) Função criar_lista()
3) Função imprimir_lista
4) Função imrpimir_pares()
5) Função imprimir_impars()
6) Função que adiciona os elementos pares em uma lista()
7) Função que adiciona os elementos impares em uma lista()
8) Função que busca um elemento na lista()
'''

def tamanho_lista():
    print('*- TAMANHO da LISTA -*')
    print('----------------------')
    t = int(input('Tamanho: '))
    return t

def criar_lista(t):
    print('*- CRIANDO uma LISTA -*')
    print('-----------------------')
    lista = [] #cria a lista vazia
    i = 0 #variável de controle
    while i < t:
        n = int(input('Número: '))
        lista.append(n)
        i += 1
    return lista


def imprimir_lista(lista):
    print('*- IMPRIMINDO a LISTA -*')
    print('-------------------------')
    for i in lista:
        print(f'Elemento: {i}')

def pares(lista):
    print('*- IMPRIMINDO PARES -*')
    print('----------------------')
    list = []
    for i in lista:
        if i % 2 == 0:
            print(f'Elemento pares: {i}')
            list.append(i)
    print(list)
    return list

def impares(lista):
    print('*- IMPRIMINDO PARES -*')
    print('----------------------')
    list = []
    for i in lista:
        if i % 2 != 0:
            print(f'Elemento impares: {i}')
            list.append(i)
    print(list)
    return list

def find_item(lista, search_item):
    for item in lista:
        if item == search_item:
            print("Sim, item está na lista")
            return True
    print("Item não encontrado!")
    return False
    
    



def principal():
    print('*- PRINCIPAL -*')
    print('---------------')
    t = tamanho_lista()
    lista = criar_lista(t)
    imprimir_lista(lista)
    pares(lista)
    impares(lista)
    item = int(input("busque um número: "))
    find_item(lista, item)
    

#Programa principal 
principal()
