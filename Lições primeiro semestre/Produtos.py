valprod = input("Valor total em produtos: ")

if int(valprod) <= 100: 
    print("valor total a ser gasto: ", int(valprod))

elif int(valprod) > 100 and int(valprod) <= 200:
    print("valor total a ser gasto: ", int(valprod)*0.9)

elif int(valprod) > 200 and int(valprod) <= 300:
    print("valor total a ser gasto: ", int(valprod)*0.8)

elif int(valprod) > 300 and int(valprod) <= 400:
    print("valor total a ser gasto: ", int(valprod)*0.7)

else: print("valor total a ser gasto: ", int(valprod)*0.6)