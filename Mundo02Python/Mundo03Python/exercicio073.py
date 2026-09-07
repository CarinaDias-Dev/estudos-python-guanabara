times = ('Palmeiras', 'Flamengo', 'Athletico-PR',
          'Fluminense', 'Bahia', 'Cruzeiro', 'Atlético-MG',
          'Bragantino', 'Coritiba', 'Corinthians', 'São Paulo',
          'Botafogo', 'Vitória', 'Santos', 'Grêmio', 'Mirassol',
          'Vasco', 'Internacional', 'Remo', 'Chapecoense')
print('{:^40}'.format('BRASILERÃO 2026'))
print('-='*20)
print(f'LISTA DE TIMES: {times}')
print('-='*20)
print(f'Os 5 primeiros colocados foram: {times[0:5]}')
print('-='*20)
print(f'Os últimos 4 colocados são: {times[-4:]}')
print('-='*20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*20)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}º posição')
print('-='*20)
