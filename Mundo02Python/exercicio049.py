#Refaça o desafio 009, mostrando a tabuada que o usuário escolher, só que agora utilizando um laço for#
num = int(input('Digite o número da tabuada: '))
print('='*12)
for c in range(0, 11):
    print(f'\033[1;34m{c} x {num} = {c*num}\033[m')
print('='*12)