listagem = list()
while True:
    numero = int(input('Digite um valor: '))
    if numero not in listagem:
        listagem.append(numero)
    else:
        print('Alistagem já tem esse número. Não irei adciona-lo.')
    resposta = input('Quer continuar? [S/N] ').upper()
    if resposta in 'N':
        break
print('=-'*30)
listagem.sort()
print(f'Os números adicionados a lista são: {listagem}')
print('=-'*30)
