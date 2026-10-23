import moeda8

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda8.moeda(p)} é {moeda8.moeda(moeda8.metade(p))}')
print(f'O dobro de {moeda8.moeda(p)} é {moeda8.moeda(moeda8.dobro(p))}')
print(f'Aumentando 10%, temos {moeda8.moeda(moeda8.aumentar(p, 10))}')
print(f'Reduzindo 13%, temos {moeda8.moeda(moeda8.diminuir(p, 13))}')
