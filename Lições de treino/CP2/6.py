nome_mais_velho = ""
idade_mais_velho = 0
sexo_mais_velho = ""

cont_alunos = 0

while cont_alunos < 5:
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    sexo = input("Digite o sexo do aluno (M/F): ")

    if idade > idade_mais_velho:
        nome_mais_velho = nome
        idade_mais_velho = idade
        sexo_mais_velho = sexo

    cont_alunos += 1


print("O aluno mais velho é:", nome_mais_velho)
print("Idade:", idade_mais_velho)
print("Sexo:", sexo_mais_velho)
