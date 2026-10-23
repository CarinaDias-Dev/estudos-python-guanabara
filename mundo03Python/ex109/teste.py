import moeda9

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda9.moeda(p)} é {moeda9.metade(p, True)}')
print(f'O dobro de {moeda9.moeda(p)} é {moeda9.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda9.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda9.diminuir(p, 13, True)}')
