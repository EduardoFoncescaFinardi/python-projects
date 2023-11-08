def coletar_notas():
    notas = input().split()
    for i in range(len(notas)):
        notas[i] = float(notas[i])
    return notas

def preenche_turma(qtde_alunos):
    turma= []
    for i in range(qtde_alunos):
        print(f'{i+1} aluno: ', end = '')
        aluno = coletar_notas()
        turma.append(aluno)
    return turma

def calcula_media(aluno):
    soma = 0
    for nota in aluno:
        soma += nota
    return soma/len(aluno)

def resumo_turma(turma):
    for aluno in turma:
        media = calcula_media(aluno)
        print(f'notas: {aluno} | média: {media}')

#main
qtde_alunos = int(input('Quantidade:'))
turma = preenche_turma(qtde_alunos)
resumo_turma(turma)