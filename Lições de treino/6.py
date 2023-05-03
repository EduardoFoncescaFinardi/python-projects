# Inicializamos as variáveis para armazenar os dados do aluno mais velho
nome_mais_velho = ""
idade_mais_velho = 0
sexo_mais_velho = ""

# Inicializamos a variável para contar quantos alunos já foram inseridos
cont_alunos = 0

# Usamos um loop while para ler os dados dos alunos
while cont_alunos < 5:
    # Pedimos os dados do aluno atual
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    sexo = input("Digite o sexo do aluno (M/F): ")

    # Verificamos se a idade do aluno é maior do que a idade do aluno mais velho encontrado até agora
    if idade > idade_mais_velho:
        # Se for, atualizamos as variáveis para armazenar os dados do aluno mais velho
        nome_mais_velho = nome
        idade_mais_velho = idade
        sexo_mais_velho = sexo

    # Incrementamos o contador de alunos
    cont_alunos += 1

# Imprimimos os dados do aluno mais velho encontrado
print("O aluno mais velho é:", nome_mais_velho)
print("Idade:", idade_mais_velho)
print("Sexo:", sexo_mais_velho)
