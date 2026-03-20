print(f'{"VENDA DE DOLLAR":=^40}')
print('\033[1;32mDESCUBRA, QUANTOS DOLARES VOCÊ CONSEGUE COMPRAR HOJE.\033[m')
carteira = float(input('Quanto dinheiro você tem? R$'))
dollar = carteira / 5.21
print('_'*30)
print(f'Com R${carteira:.2f} você pode compra hoje U${dollar:.2f}')
print('considerando o valor do dollar: U$5.21')
print('_'*30)
