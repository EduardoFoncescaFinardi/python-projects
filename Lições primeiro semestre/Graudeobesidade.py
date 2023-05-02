alt = input('altura: ')
peso = input('peso: ')

massa = int(peso)/float(alt)**2

if float(massa) < 26:
    print("Grau de obesidade: Normal")

elif float(massa) >= 26 and float(massa) <30:
    print("Grau de obesidade: Obeso")

else:
    print("Grau de obesidade: Obeso Mórbido")