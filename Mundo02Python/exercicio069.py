tot18 = menor20 = totH = 0
while True:
        idade = int(input('Informe sua idade: '))
        sexo = ' '
        while sexo not in 'FM':
            sexo = str(input('Informe o seu sexo[F/M] ')).strip().upper()[0]
        if idade >= 18:
            tot18 += 1
        if sexo == 'M':
            totH += 1
        if sexo == 'F' and idade < 20:
            menor20 += 1
        resposta = ' '
        while resposta not in 'SN':
            resposta = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
        if resposta == 'N':
            break
        print('-'*30)
print('=-'*20)
print(f'Foram cadastradas {tot18} pessoas maiores de 18 anos.')
print(f'{totH} Homens e {menor20} mulheres com menos de 20 anos.')
