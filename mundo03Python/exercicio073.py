
times = ('Flamengo', 'Palmeiras', 'Athletico-PR', 'Bahia',
         'Fluminense', 'Cruzeiro', 'Atlético-MG', 'Santos',
         'Coritiba', 'Bragantino', 'São Paulo', 'Botafogo',
         'Vitória', 'Corinthians', 'Mirassol', 'Vasco',
         'Grêmio', 'Internacional', 'Remo', 'Chapecoense')
print('-='*30)
print('LISTA DOS 20 PRIMEIROS TIMES DO BRASILEIRÃO 2026')
print('-='*30)
print(f'Os 20 primeiros colocados são: {times}')
print('='*30)
print(f'Os cinco primeiros colocados são: {times[:5]}')
print('='*30)
print(f'Os quatro ultimos colocados são: {times[-4:]}')
print('='*30)
print(f'Lista dos times em ordem alfabética: {sorted(times)}')
print('='*30)
print(f'O time da Chapecoense esta na {times.index("Chapecoense")+1}ª posição')
print('='*30)