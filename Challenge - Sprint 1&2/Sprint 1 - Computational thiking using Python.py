welcome = input("""
  Olá, somos da Porto. Menu de opções em relação a bicicletas:
  1 - Assinar serviço de seguro de bicicletas.
  2 - Já tem seguro, quero realizar vistoria.
  3 - Não quer realizar nenhum serviço em relação à bicicletas.
  Escolha uma das opções para prosseguirmos: """)


if welcome == "1":
  print("Poderia nos informar marca, tipo e número de série")
  a = input("Marca:")
  b = input("Modelo:")
  c = input("Número de série:")

if welcome == "2":
  print("Certo, lhe enviaremos para a área de identificação de dados para prosseguir para a vistoria online!")
  raise SystemExit

elif welcome == "3":
  print("Obrigado por conversar conosco, lhe enviaremos para outra assistente para você achar o serviço de seu gosto.")
  raise SystemExit

else:
  while welcome != "1" and welcome != "2" and welcome != "3":
    welcome = input("Resposta inválida, favor responder com um número de 1 a 3:")
        
    if welcome == "1":
      print("Poderia nos informar marca, tipo, número de série?")
      a = input("Marca:")
      b = input("Modelo:")
      c = input("Número de série:")

    if welcome == "2":
      print("Certo, lhe enviaremos para a área de identificação de dados para prosseguir para a vistoria!")
      raise SystemExit
    
    elif welcome == "3":
      print("Obrigado por conversar conosco, lhe enviaremos para outra assistente para você achar o serviço de seu gosto.")
      raise SystemExit
    
print("Certo, estão corretas as informações que vc nos forneceu:", a,",",b,",",c,"?")   
part2 = input("Respoder com 'S' para sim ou 'N'para não:")

if part2 == "S":
  print("Certo, lhe enviaremos para a área de identificação de dados, para assim realizar a vistoria online, obrigado por usar nossos serviços!")
  raise SystemExit

elif part2 == "N":
  print("Certo, reescreva novamente")
  a = input("Marca:")
  b = input("Modelo:")
  c = input("Número de série:")
  print("Certo, lhe enviaremos para a área de identificação de dados, para assim realizar a vistoria online. Obrigado por usar nossos serviços!")
  raise SystemExit

else:
  while part2 != "S" and part2 != "N":
    part2 = input("Respoder com 'S' para sim ou 'N'para não:")

    if part2 == "S":
      print("Certo, lhe enviaremos para a área de identificação de dados, para assim realizar a vistoria online. Obrigado por usar nossos serviços!")
      raise SystemExit
    
    elif part2 == "N":
      print("Certo, reescreva novamente")
      a = input("Marca:")
      b = input("Modelo:")
      c = input("Número de série:")
      print("Certo, lhe enviaremos para a área de identificação de dados, para assim realizar a vistoria online, obrigado por usar nossos serviços!")
      raise SystemExit


    




  

