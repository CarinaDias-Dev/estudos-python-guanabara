num = int(input('Digite um número qualquer: '))
resultado = num % 2
if resultado==1:
    print('O número \033[1;31m{}\033[m é \033[1;31mIMPAR\033[m.'.format(num))
else:
    print('O número \033[1;34m{}\033[m é \033[1;34mPAR\033[m'.format(num))
