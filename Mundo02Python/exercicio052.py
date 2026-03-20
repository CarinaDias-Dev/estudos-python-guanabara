#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo#
num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        total += 1
        print('\033[1;33m', end=' ')
    else:
        print('\033[1;31m', end=' ')
    print(c, end=' ')
print(f'\n\033[mO número {num} foi DIVISÍVEL {total} vezes')
if total == 2:
    print('\033[1;34mPor isso ELE É PRIMO!')
else:
    print('\033[1;31mPor isso ELE NÃO É PRIMO!')
