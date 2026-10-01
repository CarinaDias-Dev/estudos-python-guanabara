lista = []
pares = []
impares = []
while True:
    print('--'*20)
    elemento = lista.append(int(input('Digite um número: ')))
    resposta = input('Quer continuar? [S/N] ').upper()
    if resposta in 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-='*20)
print(f'Os elementos da sua lista são: {lista}')
print(f'Os números pares são: {pares}')
print(f'Os números impares são: {impares}')
print('-='*20)
