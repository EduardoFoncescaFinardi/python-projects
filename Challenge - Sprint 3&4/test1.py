guidao = ["guidao", "manoplas", "manete de freio", "alavanca de freio"]
quadro = ["Quadro", "Pedal", "Pedivela", "Caixa de direção", "Garfo"]
selim = ["selim", "canote", "mesa", "abraçadeira"]
rodas = ["rodas", "freio", "cambio traseiro", 'cambio dianteiro', "cassete", "corrente", "suspensão traseira"]

dictdepecas = {'Quadro': quadro, 'Guidao':guidao, 'Selim':selim, 'Rodas': rodas}

print("Selecione um grupo de peças da bicicleta para começar a declaração:")


while True:
  i = 0
  for item in dictdepecas:
    print(f'{i} - {item}')
    i+= 1

  grupopecas = int(input("Grupo de peças:"))
  grupo_selecionado = list(dictdepecas.keys())[grupopecas]

  lista_quadro = []
  lista_guidao = []
  lista_selim = []
  lista_rodas = []

  match grupopecas:
    case 0: 
      i = 0
      for item in quadro:
        print(f'{i} - {item}')
        nome_da_peça = input("Nome da peça:")
        i+= 1
        lista_quadro.append(nome_da_peça)
        print("-----------------------------")
    
    case 1:
      for item in guidao:
        print(f'{i} - {item}')
        nome_da_peça = input("Nome da peça:")
        i+= 1
        lista_guidao.append(nome_da_peça)
        print("-----------------------------")

    case 2: 
      for item in selim:
        print(f'{i} - {item}')
        nome_da_peça = input("Nome da peça:")
        i+= 1
        lista_selim.append(nome_da_peça)
        print("-----------------------------")

    case 3:
      for item in rodas:
        print(f'{i} - {item}')
        nome_da_peça = input("Nome da peça:")
        i+= 1
        lista_rodas.append(nome_da_peça)
        print("-----------------------------")


