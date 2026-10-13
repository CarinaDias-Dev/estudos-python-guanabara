def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')


print('Controle de terreno')
print('-'*20)
l = float(input('Informe a largura do terreno:(m) '))
c = float(input('Informe o comprimento do terreno:(m) '))
area(l, c)
