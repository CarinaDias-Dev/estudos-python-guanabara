alunos = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resposta in 'N':
        break
print('-'*30)
print(f'{"Nº":<3} {"NOME":^15} {"MÉDIA":>5}')
print('-'*30)
for i, a in enumerate(alunos):
    print(f'N°{i:<3} {a[0]:^10} {a[2]:7}')
while True:
    print('=-'*30)
    opçao = int(input('Qual aluno desseja consultar? (999 para sair) '))
    if opçao == 999:
        print('Finalizando...')
        break
    if opçao <= len(alunos) -1:
        print(f'Notas de {alunos[opçao][0]} são: {alunos[opçao][1]}')
print('-----FIM DO PROGRAMA!-----')
