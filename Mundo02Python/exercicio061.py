#Refaça o exercício 051, lendo o primeiro termo e a razão de um PA, mostrando os
#10 primeiros termos da progressão usando a estrutura while.
print('-'*30)
print('10 PRIMEIROS TERMOS DE UMA PA')
print('-'*30)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 1
termo = primeiro
while c <= 10:
    print(f'{termo}', end= '->')
    c += 1
    termo += razao
print('Acabou!')
