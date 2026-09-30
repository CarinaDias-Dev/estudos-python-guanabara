numeros = (int(input('Informe um número: ')),
            int(input('Informe outro número: ')), 
           int(input('Informe mais um número: ')), 
           int(input('Informe o último número: ')))
print("-="*30)
print(f'Você digitou os números: {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O número 3 apareceu na ª{numeros.index(3)+1} posição pela primeira vez')
else:
    print('O valor 3 não foi encontrado em nenhuma posição.')
print('Os números pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end='->')
print("\nfim")
print("-="*30)
