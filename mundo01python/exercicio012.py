produto = float(input('Qual o preço do produto? '))
porcentagem = (produto * 5) / 100
valor = produto - porcentagem
print('_'*50)
print('O produto que custava R${:.2f}, na promoção com 5% de desconto vai custar R${:.2f}.'.format(produto, valor))
print('_'*50)
