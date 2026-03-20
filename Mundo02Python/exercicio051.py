#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.#
print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
termo = int(input('PRIMEIRO TERMO: '))
razão = int(input('RAZÃO: '))
décimo = termo + (10 - 1) * razão
for c in range(termo, décimo + razão, razão):
    print(c, end='-> ')
print('Acabou!')

