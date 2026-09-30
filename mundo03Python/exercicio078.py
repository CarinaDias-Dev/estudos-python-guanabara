numeros = list()
maior = 0
menor = 0
for pos in range(0, 5):
    numeros.append(int(input(f'Informe um valor para a posição {pos}: ')))
    if pos == 0:
        maior = menor = numeros[pos]
    else:
        if numeros[pos] > maior:
            maior = numeros[pos]
        if numeros[pos] < menor:
            menor = numeros[pos]
print('='*30)
print(f'O maior valor digitado foi: {maior} na posição:', end='')
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i}...',end='')
print(f'\nO menor valor digitado foi: {menor} na posição: ', end='')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i}...', end='')
print('='*30)
