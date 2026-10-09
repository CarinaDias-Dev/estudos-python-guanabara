from random import randint
from time import sleep
from operator import itemgetter
jogadores = dict()
jogadores['jogador1'] = randint(1, 7)
jogadores['jogador2'] = randint(1, 7)
jogadores['jogador3'] = randint(1, 7)
jogadores['jogador4'] = randint(1, 7)

for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(1)
ranking = []
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-'*30)
print(' <<<Ranking dos jogadores:>>>')
for i, v in enumerate(ranking):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
