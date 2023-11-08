#Algoritimo de ordenação - Merge Sort (Recursivo)
#ORDENAÇÃO POR INTERCALAÇÃO/MISUTRA
#Time Complexity: 0(n*log(n))

def merge_sort(lista):
  if len(lista) > 1: #caso base

      #encontrando o meio da lista
      meio = len(lista) // 2 #divisão inteira

      #dividindo a lista em duas sublistas 
      # - fatiamente de lsitas
      L = lista[:meio]
      R = lista [meio:]

      #chamada recursiva
      merge_sort(L)

      merge_sort(R)

      #variáveis de controle
      #i - fará o controle da lsita L
      #j - fará o controle da lista R
      #K - fará o controle da lista anterior à recursão
      i = j = k = 0

      while i < len(L) and j < len(R):
        if L[i] <= R[j]:
          lista[k] = L[i]
          i += 1

        else:
          lista[k] = R[j]
          j+=1
        k+=1

        #verificação dos elementos da lista L
        while i < len(L):
          lista[k] = L[i]
          i += 1
          k+=1
        
        #verificação dos elesmentos da lista R
        while j < len(R):
          lista[k] = R[j]
          j +=1
          k +=1

#Programa Principal
lista = [12, 11, 13, 5, 6, 7]
print(f'Lista Original: {lista}')
merge_sort(lista)
print(f'Lista Ordenada {lista}')

