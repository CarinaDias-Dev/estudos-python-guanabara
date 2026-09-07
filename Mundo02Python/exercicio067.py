print('TABUADA')
while True:
    n = int(input('TABUADA DE QUAL VALOR? '))
    print('-'*20)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-'*20)
print('FIM DO PROGRAMA!')
