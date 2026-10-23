import moeda7

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda7.metade(p)}')
print(f'O dobro de {p} é {moeda7.dobro(p)}')
print(f'Aumentando 10%, temos {moeda7.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda7.diminuir(p, 13)}')
