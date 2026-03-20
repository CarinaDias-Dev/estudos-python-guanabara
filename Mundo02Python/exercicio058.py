#Melhore o desafio 028 onde o computador vai 'pensar' em um número entre 0 e 10.
#Só que agora o jogador vai tentar advinhar até acertar, mostrando no
#final quantos palpites foram necessários para vencer.
from random import randint
computador = randint(1 , 10)
print('='*50)
print(f'{"JOGO DE ADVINHAR!": ^40}')
print('='*50)
print('Olá! Eu sou o seu computador...')
print('Acabei de pensar em um número de 0 a 10. \nSerá que você consegue adivinhar qual foi?')
print('-'*50)
resposta = False
palpite = 0
c = 0
while palpite != computador:
    palpite = int(input('Qual o seu palpite? '))
    c += 1
    if palpite < computador:
        print('MAIS...')
    elif palpite > computador:
        print('MENOS...')
    elif palpite > 10:
        print('OPÇÂO INVÁLIDA! Escolha um número de 0 a 10...')
print('-'*50)
print(f'ACERTOU! Foram {c} tentativas até você acertar.')