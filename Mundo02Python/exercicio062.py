# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais
#algum termo. O programa encerra quando ele disser que quer mostrar 0 termos.
import time
from time import sleep

print('-'*20)
print('Gerador de PA')
print('-'*20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 1
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print(f'{termo}', end='-> ')
        termo += razao
        c += 1
    print('\033[1;31mPAUSE \033[m')
    mais = int(input('Mais quantos termos você quer mostrar? '))
    if mais == 0:
        print('Finalzando o programa...')
        sleep(2)
print(f'Progressão finalizada! Total de {total} termos mostrados.')
print('Obrigado! volte sempre!')
