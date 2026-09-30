#criei uma tupla com os itens e os preços, em posição intercalados, de modo que os itens ficaram em posição PAR e os preços em posição IMPAR (lembre que a posição sempre começa em 0 não em 1)
listagem = ('Lápis', 1.75,
            'Borracha',2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('='*40)
print(f'{"LISTA DE PRODUTOS":^40}')
print('='*40)

#criando um laço para cada item da tupla listagem, de modo que os da posição PAR fiquem organizados da esquerda e os preços organizados na direita
for pos in range(0, len(listagem)):  #o comando len() indica quantos elementos tem na tupla listagem.
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('='*40)
