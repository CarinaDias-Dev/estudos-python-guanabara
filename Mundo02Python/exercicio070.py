print('{:-^40}'.format('CAIXA REGISTRADORA'))
total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco >= 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
    print('-'*30)
print('=-'*20)
print(f'Valor total dos produtos R${total:.2f}')
print(f'Temos {totmil} produtos que custou mais de R$1000')
print(f'O Produto mais barato foi {barato} e tem o valor de R${menor:.2f}')
print('{:-^40}'.format('FIM DO PROGRAMA'))
