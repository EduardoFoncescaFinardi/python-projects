quadro = ["Quadro", "Pedal", "Pedivela", "Caixa de direção", "Garfo", "Movimento Central"]
guidao = ["Guidão", "Manoplas", "Manete de Freio", "Alavanca de Freio"]
selim = ["Selim", "Canote", "Mesa", "Abraçadeira"]
rodas = ["Rodas", "Freio", "Câmbio Traseiro", 'Câmbio Dianteiro', "Cassete", "Corrente", "Suspensão Traseira"]

print("""Certo! Agora começará uma série de perguntas relacionadas 
a cada parte da sua bicicleta para você declarar cada peça.""")
print("---------------------------------------------------------------")
responseData = {
        "Quadro": [],
        "Guidão": [],
        "Selim": [],
        "Rodas": [],
    }

for i in range(0,4):

    match i:
        case 0: 
            i = 0
            for item in quadro:
                print(f'Item de decleração, {item};')
                nome_da_peça = input("Nome da peça:")
                responseData["Quadro"].append(nome_da_peça)
                print("-----------------------------")
            
            print("Verifique se todos os itens estão corretos:")
            j = 0
            for items in responseData["Quadro"]:
                print(f'{j} - {items}')
                j += 1
            question = input("(S)im ou (N)ão:")
            while question != "S" and question != "N":
                print("Opção inválida! Apenas 'S' para sim e 'N' para não!")
                question = input("(S)im ou (N)ão:")
            if question == "S":
                continue
            elif question =="N":
                quantida_de_pecas_erradas = int(input("Quantas peças estão erradas?:"))
                if quantida_de_pecas_erradas > 0:
                    for i in range(quantida_de_pecas_erradas):
                        peca_errada = int(input(f"Digite o índice do item errado (0 a 5): "))
                        if 0 <= peca_errada < len(responseData["Quadro"]):
                            correction = input(f"Digite a correção para o item {peca_errada}: ")
                            responseData["Quadro"][peca_errada] = correction
                print("-----------------------------")
                print("peças corrigidas!!")
                j = 0
                for items in responseData["Quadro"]:
                    print(f'{j} - {items}')
                    j += 1
                print("Daremos sequência a pesquisa")
                print("-----------------------------")

        case 1:
            for item in guidao:
                print("-----------------------------")
                print(f'Item de decleração, {item};')
                nome_da_peça = input("Nome da peça:")
                responseData["Guidão"].append(nome_da_peça)
            
            print("Verifique se todos os itens estão corretos:")
            j = 0
            for items in responseData["Guidão"]:
                print(f'{j} - {items}')
                j += 1
            question = input("(S)im ou (N)ão:")
            while question != "S" and question != "N":
                print("Opção inválida! Apenas 'S' para sim e 'N' para não!")
                question = input("(S)im ou (N)ão:")
            if question == "S":
                continue
            elif question =="N":
                quantida_de_pecas_erradas = int(input("Quantas peças estão erradas?:"))
                if quantida_de_pecas_erradas > 0:
                    for i in range(quantida_de_pecas_erradas):
                        peca_errada = int(input("Digite o índice do item errado (0 a 3): "))
                        if 0 <= peca_errada < len(responseData["Guidão"]):
                            correction = input(f"Digite a correção para o item {peca_errada}: ")
                            responseData["Guidão"][peca_errada] = correction
                print("-----------------------------")
                print("peças corrigidas!!")
                j = 0
                for items in responseData["Guidão"]:
                    print(f'{j} - {items}')
                    j += 1
                print("Daremos sequência a pesquisa")
                print("-----------------------------")

        case 2: 
            for item in selim:
                print(f'Item de decleração, {item};')
                nome_da_peça = input("Nome da peça:")
                responseData["Selim"].append(nome_da_peça)
                print("-----------------------------")
            
            print("Verifique se todos os itens estão corretos:")
            j = 0
            for items in responseData["Selim"]:
                print(f'{j} - {items}')
                j += 1
            question = input("(S)im ou (N)ão:")
            while question != "S" and question != "N":
                print("Opção inválida! Apenas 'S' para sim e 'N' para não!")
                question = input("(S)im ou (N)ão:")
            if question == "S":
                continue
            elif question =="N":
                quantida_de_pecas_erradas = int(input("Quantas peças estão erradas?:"))
                if quantida_de_pecas_erradas > 0:
                    for i in range(quantida_de_pecas_erradas):
                        peca_errada = int(input("Digite o índice do item errado (0 a 3): "))
                        if 0 <= peca_errada < len(responseData["Selim"]):
                            correction = input(f"Digite a correção para o item {peca_errada}: ")
                            responseData["Selim"][peca_errada] = correction
                print("-----------------------------")
                print("peças corrigidas!!")
                j = 0
                for items in responseData["Selim"]:
                    print(f'{j} - {items}')
                    j += 1
                print("Daremos sequência a pesquisa")
                print("-----------------------------")


        case 3:
            for item in rodas:
                print(f'Item de decleração, {item};')
                nome_da_peça = input("Nome da peça:")
                responseData["Rodas"].append(nome_da_peça)
                print("-----------------------------")

            print("Verifique se todos os itens estão corretos:")
            j = 0
            for items in responseData["Rodas"]:
                print(f'{j} - {items}')
                j += 1
            question = input("(S)im ou (N)ão:")
            while question != "S" and question != "N":
                print("Opção inválida! Apenas 'S' para sim e 'N' para não!")
                question = input("(S)im ou (N)ão:")
            if question == "S":
                continue
            elif question =="N":
                quantida_de_pecas_erradas = int(input("Quantas peças estão erradas?:"))
                if quantida_de_pecas_erradas > 0:
                    for i in range(quantida_de_pecas_erradas):
                        peca_errada = int(input("Digite o índice do item errado (0 a 6): "))
                        if 0 <= peca_errada < len(responseData["Rodas"]):
                            correction = input(f"Digite a correção para o item {peca_errada}: ")
                            responseData["Rodas"][peca_errada] = correction
                print("-----------------------------")
                print("peças corrigidas!!")
                j = 0
                for items in responseData["Rodas"]:
                    print(f'{j} - {items}')
                    j += 1
                print("Daremos sequência a pesquisa")
                print("-----------------------------")

    i += 1



        
