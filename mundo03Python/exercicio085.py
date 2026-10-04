numeros = [[],[]]
valor = 0
for n in range(1, 8):
    valor = int(input(f'Digite o {n}º numero: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print('='*40)
numeros[0].sort()
numeros[1].sort()
print(f'Os numeros pares digitados são {numeros[0]}')
print(f'Os números impares digitados são: {numeros[1]}')
