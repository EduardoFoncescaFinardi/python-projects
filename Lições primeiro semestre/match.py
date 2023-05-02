print("Cálculo de média")

n1 = float(input("nota 1: "))
n2 = float(input("nota 2: "))
n3 = float(input("nota 3: "))

med = (n1+n2+n3)/3

print("Média: " , med)

if med >= 9:
  conceito = "A"

elif med >= 8 and med <= 8.9:
  conceito = "B"

elif med >= 7 and med <= 7.9:
  conceito = "C"

elif med >= 6 and med <=6.9:
  conceito = "D"

elif med >= 2 and med <=5.9:
  conceito = "E"

else :
  conceito = "F"

match conceito:
  case "A":
    print("Conceito: ", conceito)
  case "B":
    print("Conceito: ", conceito)
  case "C":
    print("Conceito: ", conceito)
  case "D":
     print("Conceito: ", conceito)
  case"E":
     print("Conceito: ", conceito)
  case "F":
     print("Conceito: ", conceito)