n1 = int(input("Primeiro número: "))

Op = input("Operador:")

n2 = int(input("Segundo número:"))

if Op == "+":
    print("A Soma é:", n1 + n2)

elif Op == "-":
    print("A subtração é:", n1 - n2)

elif Op == "*":
    print("A multiplicação é:", n1 * n2)

elif Op == "/":
    print("A divisão é:", n1 / n2)

else:
    print("Operador inválido!")
