#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#o primeiro valor é maior
#o segundo valor é maior
#Não existe valor maior, os dois são iguais

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print(f'O PRIMEIRO número \033[1;34m{n1}\033[m é o MAIOR.')
    print(f'O SEGUNDO número \033[1;33m{n2}\033[m é o MENOR')
elif n2 > n1:
    print(f'O SEGUNDO número \033[1;34m{n2}\033[m é o MAIOR.')
    print(f'O PRIMEIRO número \033[1;33m{n1}\033[m é o MENOR')
else:
    print('Não existe valor maior ou menor! \033[1;34mOS DOIS NÚMEROS SÃO IGUAIS.\033[m')
