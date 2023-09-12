guidao = ["guidao", "manoplas", "manete de freio", "alavanca de freio"]
quadro = ["Quadro", "Pedal", "Pedivela", "Caixa de direção", "Garfo"]
selim = ["selim", "canote", "mesa", "abraçadeira"]
rodas = ["rodas", "freio", "cambio traseiro", 'cambio dianteiro', "cassete", "corrente", "suspensão traseira"]

dictdepecas = {'Quadro': quadro, 'Guidao': guidao, 'Selim': selim, 'Rodas': rodas}

print("Selecione um grupo de peças da bicicleta para começar a declaração:")

while True:
    i = 0
    for item in dictdepecas:
        print(f'{i} - {item}')
        i += 1

    grupopecas = int(input("Grupo de peças (ou -1 para sair): "))

    if grupopecas == -1:
        break

    grupo_selecionado = list(dictdepecas.keys())[grupopecas]

    lista_peca = []

    for item in dictdepecas[grupo_selecionado]:
        print(f'{i} - {item}')
        nome_da_peca = input("Nome da peça:")
        i += 1
        lista_peca.append(nome_da_peca)
        print("-----------------------------")

    dictdepecas.pop(grupo_selecionado)  

    print(f"Peças do grupo {grupo_selecionado}: {lista_peca}")
    print("Grupos restantes:")
