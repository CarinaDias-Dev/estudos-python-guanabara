#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. no final do programa mostre:
#A média de idade do grupo.  -quantas mulheres têm menos de 20 anos  -Qual é o nome do homem mais velho
somaidade = 0
mediaidade = 0
idadehomemvelho = 0
nomehomemvelho = ''
somamulher = 0
for p in range(1, 5):
    print(f'-------{p}ª--------')
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('Sexo[F/M]')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        idadehomemvelho = idade
        nomehomemvelho = nome
    if sexo in 'Mm' and idade > idadehomemvelho:
        idadehomemvelho = idade
        nomehomemvelho = nome
    if sexo in 'F,f' and idade < 20:
        somamulher += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é {mediaidade}')
print(f'O homem mais velho é {nomehomemvelho} que tem {idadehomemvelho} anos')
print(f'{somamulher} mulheres tem menos de 20 anos')
