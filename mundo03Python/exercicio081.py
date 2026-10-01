lista = list()
while True:
    print('--'*20)
    elemento = lista.append(int(input('Informe um valor para a sua lista: ')))
    lista.sort(reverse=True)
    resposta = input('Quer continuar? [S/N] ').upper()
    if resposta in 'N':
        break
print('-='*20)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os elementos da sua lista são: {lista}')
if 5 in lista:
    print('O elemento 5 está na sua lista.')
else:
    print('O elemento 5 NÃO está presente na lista.')
print('-='*20)
