print("""
-------------------------** APRESENTACAO **-------------------------
            Olá, Bem-vindo ao Projeto Localiza&Auxilia!
  
Aqui pretendemos te auxiliar da melhor maneira de como se informar sobre 
a situação de produção, venda e transportes alimentícios de onde você habita, portanto 
faremos uma série de perguntas relacionadas a sua vida pessoal.

*Dicas de uso:*
- Para perguntas de sim ou não, usar 'S' para sim e 'N' para não!;
- Para perguntas que envolvam qualquer tipo de lista, responder com o número de desejo.
""")

def cadastro_pessoais_usuario():
  
  print("------------------------------------------------------------")
  print("nos informe, por gentileza(dados obrigatórios!)")
  nome = input("seu nome: ")
  data_nasc = input("sua data de nascimento: ")
  e_mail = input("E-mail:")
  list = [nome, data_nasc, e_mail]
  print("-------------------------------------")
  print("Estão corretos, os dados abaixo, de acordo com a ordem de preenchimento?")
  print(list)
  confirmacao = input("Estão corretos?:")
  
  while confirmacao != "S" and confirmacao != "N":
    print("------------------------------------------------------------")
    print("Resposta inválida! Responder apenas com 'S' para sim e 'N' para não.") 
    print(f'''Seu nome: {nome}, sua data de nascimento: {data_nasc} e seu e-mail:{e_mail}''')
    confirmacao = input("Estão corretos?:")
  
  return confirmacao

def localizao_macro(confirmacao):
  
  if confirmacao == "S":
    print("------------------------------------------------------------")
    print("Certo! Daremos sequência a pesquisa.")
  
  while confirmacao == "N":
    print("------------------------------------------------------------")
    print("""Por favor preencha novamente os campos abaixo!""")
    print("nos informe, por gentileza")
    nome = input("seu nome: ")
    data_nasc = input("sua data de nascimento: ")
    e_mail = input("E-mail:")
    print(f'''Seu nome: {nome}, sua data de nascimento: {data_nasc} e seu e-mail:{e_mail}''')
    confirmacao = input("Estão corretos?:")

  
  print("------------------------------------------------------------")
  print("""Certo, agora selecione a região a qual você pertence
1 - Norte
2 - Nordeste
3 - Centro-Oeste
4 - Sudeste
5 - Sul""")
     
  regiao = int(input("Escolha uma:"))
  while regiao not in range (1,6):
      print("Escolha apenas um dos números acima!")
      regiao = int(input("Escolha um:"))
  
  print("------------------------------------------------------------")

  return regiao
      
def selecao_bioma(regiao):
  
  match regiao:
    case 1:
        print("""Escolha o bioma que você reside:
1 - Floresta Amazônica
2 - Cerrado(1)""")
        bioma = int(input("Escolha um:")) 
        while bioma not in (1,2):
          print("Escolha apenas um dos números acima!")
          bioma = int(input("Escolha um:"))
    
    case 2:
        print("""Escolha o bioma que você reside:
3 - Caatinga
4 - Mata Atlântica(1)""")
        bioma = int(input("Escolha um:")) 
        while bioma not in (3,4):
          print("Escolha apenas um dos números acima!")
          bioma = int(input("Escolha um:"))
    
    case 3:
        print("""Escolha o bioma que você reside:
5 - Cerrado(2)
6 - Pantanal""")
        bioma = int(input("Escolha um:")) 
        while bioma not in (5,6):
          print("Escolha apenas um dos números acima!")
          bioma = int(input("Escolha um:"))

    case 4:
        print("""Escolha o bioma que você reside:
7 - mata atlantica(2)
8 - Cerrado(3)""")
        bioma = int(input("Escolha um:")) 
        while bioma not in (7,8):
          print("Escolha apenas um dos números acima!")
          bioma = int(input("Escolha um:"))

    case 5:
        print("""Escolha o bioma que você reside:
9 - Mata Atlântica(3)
10 - Pampas""")
        bioma = int(input("Escolha um:")) 
        while bioma not in (9,10):
          print("Escolha apenas um dos números acima!")
          bioma = int(input("Escolha um:"))
  
  print("------------------------------------------------------------")
  
  return bioma

def informacoes_biomas(bioma):
  
  match bioma:
    case 1:
        with open('floresta_amazonica.md', "r", encoding = "utf-8") as arquivo:
            conteudo = arquivo.read() 
        print(conteudo)
    
    case 2:
        with open('cerrado_1.md', "r", encoding = "utf-8") as file:
            content = file.read()
        print(content)
    
    case 3:
        with open('caatinga.md', "r", encoding = "utf-8") as file:
            content = file.read()
        print(content)
    
    case 4:
        with open('mata_atlantica_1.md', "r", encoding = "utf-8") as file:
            content = file.read()
        print(content)
    
    case 5:
        with open('cerrado_2.md', "r", encoding = "utf-8") as file:
            content = file.read()
        print(content)

    case 6:
        with open('pantanal.md', "r", encoding = "utf-8") as file:
            content = file.read()
        print(content)
    
    case 7:
        with open('mata_atlantica_2.md', "r", encoding = "utf-8") as file:
            content = file.read() 
        print(content)
    
    case 8:
        with open('cerrado_3.md', "r", encoding = "utf-8") as file:
            content = file.read()
        print(content)
    
    case 9:
        with open('mata_atlantica_3.md', "r", encoding = "utf-8") as file:
            content = file.read()
        print(content)
    
    case 10:
        with open('pampas.md', "r", encoding = "utf-8") as file:
            content = file.read()
        print(content)
    

def main():
    Confirmacao = cadastro_pessoais_usuario()
    repetir_processo = "S"
    while repetir_processo == "S": 
        regiao = localizao_macro(Confirmacao)
        bioma = selecao_bioma(regiao)
        informacoes_biomas(bioma)
        repetir_processo = input("Gostaria de refazer a pesquisa?: ")
        while repetir_processo != "S" and repetir_processo != "N":
            print("------------------------------------------------------------")
            print("Use, apenas, 'S' para sim e 'N' para não!")
            repetir_processo = input("Gostaria de refazer a pesquisa?: ")
        if repetir_processo == "N":
            break    

main()

