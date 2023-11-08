def menu():
    selecao = int(input("""
*-- MENU --*

1 - realizar vistoria, em caso de acidente;
2 - realizar vistoria, em caso de renovação de seguro;
3 - realizar vistoria, em caso de furto/roubo;
4 - realizar vistoria, em caso de primeiro seguro. 

(Em caso de respostas de sim ou não, respoder 
com 'S' para sim e 'N' para não!)


Selecionar item de acordo com necessidade: """))
    while selecao not in [1, 2, 3, 4]:
        print("------------------------------------")
        print("Selecione apenas as opções de 1 a 3!")
        selecao = int(input("""
*-- MENU --*

1 - realizar vistoria, em caso de acidente;
2 - realizar vistoria, em caso de renovação de seguro;
3 - realizar vistoria, em caso de furto/roubo; 

Selecionar item de acordo com necessidade: """))
    return selecao

def selecao_menu_1(selecao):
    if selecao == 1:
      print("------------------------------------------------------")
      listadepecas = ["Quadro", "Guidão", "Manoplas", "Manete de Freio", "Alavanca de Câmbio", "Mesa",
                        "Headset ou Caixa de Direção", "Garfo", "Rodas", "Freio", "Câmbio Dianteiro", 
                          "Câmbio Traseiro", "Cassete", "Corrente", "Movimento Central", "Pedivela", "Pedal",
                            "Selim", "Canote de Selim", "Abraçadeira de Selim", "Suspensão Traseira"]
      
      qntpecas = int(input("Quantidade de peças danificadas: "))
      
      while qntpecas < 0 or qntpecas > len(listadepecas):
        print("Quantidade inválida! Máximo de 21 peças!")
        qntpecas = int(input("Quantidade de peças danificadas: "))

      quaispecas = []
     
      print("------------------------------------------------------")
      print("""
Certo! Agora declare qual(is) peça(s) foi(foram) danificada:
      1 - Quadro
      2 - Guidão
      3 - Manoplas
      4 - Manete de Freio
      5 - Alavanca de Câmbio
      6 - Mesa
      7 - Headset ou Caixa de Direção
      8 - Garfo
      9 - Rodas
      10 - Freio
      11 - Câmbio Dianteiro
      12 - Câmbio Traseiro
      13 - Cassete
      14 - Corrente
      15 - Movimento Central
      16 - Pedivela
      17 - Pedal
      18 - Selim
      19 - Canote de Selim
      20 - Abraçadeira de Selim
      21 - Suspensão Traseira
        """)

      for i in range(qntpecas):

        opcao = int(input("Peça(s): "))
        while opcao < 1 or opcao > len(listadepecas):
          print("Opção inválida! Escolha um número válido.")
          opcao = int(input("Peça(s): "))

        quaispecas.append(listadepecas[opcao - 1])

      print("As peças danificadas, são:", quaispecas, "Certo?")
      question = input("(S)im ou (N)ão:")
      while question != "S" and question != "N":
        print("Opção inválida! Apenas 'S' para sim e 'N' para não!")
        question = input("(S)im ou (N)ão:")
      
      print("------------------------------------------------------")

      print("""Obrigado por se utilizar de nossos serviços!
O encaminharemos para o setor de upload de fotos
para darmos sequência a vistoria!""")

      
      
    

def selecao_menu_2(selecao):
    listadepecas = ["Quadro", "Guidão", "Manoplas", "Manete de Freio", "Alavanca de Câmbio", "Mesa",
                        "Caixa de Direção", "Garfo", "Rodas", "Freio", "Câmbio Dianteiro", 
                          "Câmbio Traseiro", "Cassete", "Corrente", "Movimento Central", "Pedivela", "Pedal",
                            "Selim", "Canote de Selim", "Abraçadeira de Selim", "Suspensão Traseira"]
    
    if selecao == 2:
      print("------------------------------------------------------------")

      alteração = input("""Houve alguma alteração
em relação a bicicleta usada no seguro anterior?:""")
      if alteração == "N":
        print("Certo! O encaminharemos para o setor de upload de fotos para darmos sequência a vistoria!")

      elif alteração == "S":
        qntpecas = int(input("Quantidade de peças danificadas: "))
      
      while qntpecas < 0 or qntpecas > len(listadepecas):
        print("Quantidade inválida! Máximo de 21 peças!")
        qntpecas = int(input("Quantidade de peças alteradas: "))

      quaispecas = []
     
      print("------------------------------------------------------")
      print("""
Certo! Agora declare qual(is) peça(s) foi(foram) danificada:
      1 - Quadro
      2 - Guidão
      3 - Manoplas
      4 - Manete de Freio
      5 - Alavanca de Câmbio
      6 - Mesa
      7 - Caixa de Direção
      8 - Garfo
      9 - Rodas
      10 - Freio
      11 - Câmbio Dianteiro
      12 - Câmbio Traseiro
      13 - Cassete
      14 - Corrente
      15 - Movimento Central
      16 - Pedivela
      17 - Pedal
      18 - Selim
      19 - Canote de Selim
      20 - Abraçadeira de Selim
      21 - Suspensão Traseira
        """)

      for i in range(qntpecas):

        opcao = int(input("Peça(s): "))
        while opcao < 1 or opcao > len(listadepecas):
          print("Opção inválida! Escolha um número válido.")
          opcao = int(input("Peça(s): "))

        quaispecas.append(listadepecas[opcao - 1])

      print("As peças alteradas, são:", quaispecas, ",Certo?")
      question = input("(S)im ou (N)ão:")
      while question != "S" and question != "N":
        print("Opção inválida! Apenas 'S' para sim e 'N' para não!")
        question = input("(S)im ou (N)ão:")
      
      print("Certo! nos envie os dados, com as marcas das peças novas, na mesma ordem da lista a seguir:", quaispecas)
      list = []
      i = 0
      
      while len(list) < len(quaispecas):
        marcas = input("Marcas: ")
        list.append(marcas)
        i += 1
            
      print("As marcas que compõe sua bicicleta, são", list , "Correto?")
      question = input("(S)im ou (N)ão:")
      while question != "S" and question != "N":
          print("Opção inválida! Apenas 'S' para sim e 'N' para não!")
          question = input("(S)im ou (N)ão:")
      print("------------------------------------------------------")

      print("""Obrigado por se utilizar de nossos serviços!
O encaminharemos para o setor de upload de fotos
para darmos sequência a vistoria!""")

def selecao_menu_3(selecao):
    if selecao == 3:
      case = print("Caso sua bicicleta tenha sido furtada/roubada, teremos que analisar a situação!")
      local = input("Em qual local ocorreu?:")
      data =input("Em qual dia?:")
      BO = input("Já fez B.O. policial(responder com 'S' ou 'N'?:")
      if BO == "S":
        input("Nos envie o número do protocolo:")
        print("Certo, daremos sequência ao seu caso!")
        print("O encaminharemos para o setor responsável pelo caso! Obrigado por utilizar nossos serviços!")

      elif BO == "N":
        print("Recomendamos que faça e volte aqui para darmos sequência ao seu processo!")
        print(" Obrigado por utilizar nossos serviços!")

      while BO != "S" and BO != "N":
        print("Opção inválida! Apenas 'S' para sim e 'N' para não!")
        BO = input("Já fez B.O. policial(responder com 'S' ou 'N'?:")
        if BO == "S":
          input("Nos envie o número do protocolo:")
          print("Certo, daremos sequência ao seu caso!")
          print("O encaminharemos para o setor responsável pelo caso! Obrigado por utilizar nossos serviços!")

        elif BO == "N":
          print("Recomendamos que faça e volte aqui para darmos sequência ao seu processo!")
          print(" Obrigado por utilizar nossos serviços!")

def selecao_menu_4(selecao):
    print("---------------------------------------------------------------")

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


def main():
    selecao = menu()
    selecao_menu_1(selecao)
    selecao_menu_2(selecao)
    selecao_menu_3(selecao)
    selecao_menu_4(selecao)

main()
        
