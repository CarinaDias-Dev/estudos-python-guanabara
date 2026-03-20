distancia =  float(input('Quantos km Tem a sua viagem? '))
'''longas = 0.45*distancia
perto = 0.50*distancia
print('Você está prestes a começar uma viagem de {:.0f}Km'.format(distancia))
if distancia >200:
    print('O preço da passagem será: R${:.2f}'.format(longas))
else:
    print('O preço da pasagem será: R${:.2f}'.format(perto))'''

print('Você está prestes a começar uma viagem de \033[1;32m{}Km\033[m.'.format(distancia))
preço = distancia*0.50 if distancia<= 200 else distancia*0.45
print('O preço da sua passagem será \033[4;33mR${:.2f}\033[m'.format(preço))
