numeros = []
impares = []
pares = []
for n in range(0, 7):
    numeros.append(int(input(f'Informe um {n+1}º número: ')))
for p in numeros:
    if p % 2 == 0:
        pares.append(p)
        pares.sort()
    else:
        impares.append(p)
        impares.sort()
numeros.clear()
numeros.append(pares[:])
numeros.append(impares[:])
print('≃~'*30)
print(f'Os valores pares digitados foram {numeros[0]}')
print(f'Valores impares digitados {numeros[1]}')
