#Crie um programa que faça o computador jogar JOKENPÔ com você#
from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print(f'{"VAMOS JOGAR JOKENPÔ?":=^40}')
print('''START
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)
print('-='*11)
print(f'O COMPUTADOR ESCOLHEU : {itens[computador]}')
print(f'O JOGADOR ESCOLHEU: {itens[jogador]}')
print('-='*11)
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('PAPEL VENCE PEDRA. O JOGADOR VENCEU! ')
    elif jogador == 2:
        print('PEDRA VENCE TESOURA. O COMPUTADOR VENCEU!')
elif computador == 1:
    if jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('TESOURA GANHA DE PAPEL. O JOGADOR VENCEU!')
    elif jogador == 0:
        print('PAPEL VENCE PEDRA. O COMPUTADOR VENCEU!')
elif computador == 2:
    if jogador == 2:
        print('EMPATE!')
    elif jogador == 0:
        print('PEDRA VENCE TESOURA. O JOGADOR VENCEU!')
    elif jogador == 1:
        print('TESOURA VENCE PAPEL. O COMPUTADOR VENCEU!')

