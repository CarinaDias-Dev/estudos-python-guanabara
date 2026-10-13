def ficha(nome='<desconhecido>', gol=0):
    print('-='*20)
    print(f'O jogador {nome} marcou {gol} golls.')

n = str(input('Nome do jogador: '))
g = str(input(f'Quantos gols o jogador {n} marcou? '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
