matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma_par = coluna_tres = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Informe o número para [{l, c}]: '))
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
        else:
            if len(matriz[1]) == 0:
                matriz[1][0] == maior
            else:
                if matriz[1][1] > maior:
                    maior = matriz[1][1]
                if matriz[1][2] > maior:
                    maior = matriz[1][2]
for l in range(0,3):
    coluna_tres += matriz[l][2]
print('='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('='*30)
print(f'A soma dos números Pares é {soma_par}')
print(f'O maior número da segunda linha é {maior}')
print(f'A soma da terceira coluna é {coluna_tres}')



