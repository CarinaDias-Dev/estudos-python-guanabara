print('='*70)
print(f'{"PINTURA!": ^70}')
print('='*70)
print('\033[1;32mDESCUBRA QUANTOS LITROS \033[1;35mDE TINTA IRÁ PRECISAR\033[1;34m PARA PINTAR SUA PAREDE.\033[m')
print('='*70)
largura = float(input('Qual a largura: '))
altura = float(input('Qual a altura: '))
area = largura*altura
print('_'*40)
print(f'A sua parede tem a dimensão de {largura:.1f} x {altura:.1f} e a área de {area:.1f}m²')
tinta = area/2
print(f'Para pitar essa parede você irá precisar de {tinta} litros de tinta.')
print('_'*40)
