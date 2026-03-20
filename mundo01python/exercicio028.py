from random import randint
computador = randint(0,5) #Faz o computador pensar
print('~~'*20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar....')
print('~'*20)
jogador = int(input('Em que número eu pensei? ')) # O jogador tenta advinhar
if jogador == computador:
    print('Você \033[4;34macertou!\033[m O número é \033[32m{}\033[m. \033[35mPARABÉNS!\033[m'.format(computador))
else:
    print('\033[1;31mVocê errou!\033[m O número é \033[33m{}\033[m'.format(computador))
