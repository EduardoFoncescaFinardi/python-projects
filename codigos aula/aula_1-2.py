def tamanho_lista():
    print('TAMANHO DA LISTA')
    print('-----------------')
    t = int(input('Tamanho: '))
    return t

def criar_lista(t):
    print('CRIAR uma LISTA')
    print('-----------------')
    lista = []
    i=0
    while i < t:
        n = int(input('Número: '))
        lista.append(n)
        i+=1
    return lista

def imprimir_lista(lista):
    print('IMPRIMIR A LISTA')
    print('-----------------')
    for i in lista:
        print(f'Elemento: {i}')

def imprimir_pares(lista):
    print('IMPRIMIR os ELEMENTOS PARES da LISTA')
    print('-------------------------------------')
    for i in lista:
        if i%2 == 0:
            print(f'{i} é PAR!')

def separar_pares(lista):
    print('SEPARANDO os ELEMENTOS PARES')   
    print('----------------------------')    
    lista_pares = []    
    for i in lista: 
        if i%2 == 0:
            lista_pares.append(i)
    return lista_pares

def obter_numero():
    print('OBTER um NÚMERO') 
    print('---------------')  
    n = int(input('Número: '))
    return n

def verificar_qtde_ocorrencias(lista, n):
    print('QUANTIDADE DE OCORRÊNCIAS DE UM NÚMERO')
    print('-------------------------------------')
    cont = 0
    for i in lista:
        if i == n:
            cont +=1
    return cont

def principal():
    print('PRINCIPAL')
    print('-----------------')
    tamanho = tamanho_lista()
    minha_lista = criar_lista(tamanho)
    imprimir_lista(minha_lista)
    print(f'Tamanho: {len(minha_lista)}')
    imprimir_lista(minha_lista)
    lista_pares = separar_pares(minha_lista)
    imprimir_lista(lista_pares)
    n = obter_numero()
    qtde = verificar_qtde_ocorrencias(minha_lista, n)
    print(f'Qtde: {qtde}')

principal()