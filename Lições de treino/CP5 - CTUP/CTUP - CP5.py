import random
import time

def algoritmo_escolha():
  print('Escolha um algoritmo:')
  print('1 - Bubble Sort')
  print('2 - Selection Sort')
  print('3 - Insertion Sort')
  print('4 - Merge Sort')
  escolha = int(input('Sua escolha: '))
  return escolha

def bubbleSort(lista):
    tam = len(lista)
    for i in range(tam-1):
        troca = False
        for j in range(0, tam-i-1):
            if lista[j] > lista[j+1]:
                troca = True
                lista[j], lista[j+1] = lista[j+1], lista[j]
        if not troca:
            return

def selectionSort(lista):
    for i in range(len(lista)):
        min_index = i
        for j in range(i+1, len(lista)):
            #seleciona o menor elemento em cada interação
            if lista[j] < lista[min_index]:
                min_index = j
        #troca os elementos - atribuição paralela
        lista[i], lista[min_index] = lista[min_index], lista[i]

def insertionSort(lista):
    for i in range(1, len(lista)):
        pivo = lista[i]
        j = i-1
        while j>=0 and pivo<lista[j]:
            lista[j+1] = lista[j]
            j-=1
        lista[j+1] = pivo

def mergeSort(lista):
    if len(lista) > 1:

        #encontrando o meio da lista
        meio = len(lista) // 2

        #dividindo a lista em 2 sublistas (L e R)
        L = lista[:meio]
        R = lista[meio:]
        mergeSort(L)
        mergeSort(R)

        #variaveis de controle:
        #i - fará o controle da lista L
        #j - fará o controle da lista R
        #k - fará o controle da lista anterior a recursão
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                lista[k] = L[i]
                i+=1
            else:
                lista[k] = R[j]
                j+=1
            k+=1

        #verificação da lista L
        while i < len(L):
            lista[k] = L[i]
            i+=1
            k+=1

        #verificação da lista R
        while j < len(R):
            lista[k] = R[j]
            j+=1
            k+=1

def encaminhamento_da_escolha(escolha, lista):
  match escolha:
    case 1:
      bubbleSort(lista)
      print("---------------------------")
      print("Método escolhido: BubbleSort")
      return lista
    case 2:
      selectionSort(lista) 
      print("---------------------------")
      print("Método escolhido: SelectionSort")  
      return lista
    case 3:
      insertionSort(lista)
      print("---------------------------")
      print("Método escolhido: InsertionSort")      
      return lista

    case 4:
      mergeSort(lista)
      print("---------------------------")
      print("Método escolhido: MergeSort")      
      return lista

def print_dados(lista):
  inicio = time.time()
  print(f'Lista ordenada: {lista}')
  print("---------------------------")
  fim = time.time()
  tempo = round(fim - inicio, 3)
  print(f'Tempo de execução: {tempo}')
  print("---------------------------")

def main():
  repetir_processo = "S"
  while repetir_processo == "S": 
    lista = list(range(0,1000000))
    random.shuffle(lista)

    escolha = algoritmo_escolha()
    print("---------------------------")
    print(f'Lista original: {lista}')
    lista = encaminhamento_da_escolha(escolha, lista)
    print_dados(lista)
    repetir_processo = input("Gostaria de refazer a pesquisa?: ")
    while repetir_processo != "S" and repetir_processo != "N":
        print("------------------------------------------------------------")
        print("Use, apenas, 'S' para sim e 'N' para não!")
        repetir_processo = input("Gostaria de refazer a pesquisa?: ")
    if repetir_processo == "N":
        break    

main()