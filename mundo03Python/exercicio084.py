temporaria = []
principal = []
menor = maior = 0
while True:
    temporaria.append(input('Nome: '))
    temporaria.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        if temporaria[1] < menor:
            menor = temporaria[1]
    principal.append(temporaria[:])
    temporaria.clear()
    resposta = input('Deseja continuar? [S/N] ').upper()
    if resposta in 'N':
        break
print('=~'*30)
print(f'Foram cadastradas {len(principal)} pessoas.')
print(f'O maior peso cadastrado foi {maior} KG. De ', end='')
for p in principal:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso cadastrado foi {menor} KG. De ', end=' ')
for p in principal:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
print()
