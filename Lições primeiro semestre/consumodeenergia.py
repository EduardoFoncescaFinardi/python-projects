con = int(input("Qual foi seu consumo (KWh)?:"))

if con < 150:
    valor = con * 0.2
elif con >= 150 and con < 500:
    valor = con * 0.25
else:
    valor = con * 0.3

if valor < 11.9:
    print("Valor a ser pago: 11.9")
else:
    ("Valor a ser pago: ", valor)
    