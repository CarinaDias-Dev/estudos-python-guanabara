#Crie um programa que leia dois valores e mostre um menu como o seguinte:
#[1]somar
#[2]multiplicar         >>>>seu programa deverá realizar a operção solicitada em cada caso.<<<<<<
#[3]maior
#[4]novos números
#[5]sair do programa
from time import sleep
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Segundo valor: '))
opção = 1
while opção != 5:
    print('=-='*20)
    print(f'{"OPÇÕES:": ^20}')
    print('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opção = int(input('DIGITE A OPÇÃO: '))
    if opção == 1:
        resposta = num1 + num2
        print(f'\033[1;34mA soma de {num1} + {num2} = {resposta}\033[m')
    elif opção == 2:
        resposta = num1 * num2
        print(f'\033[1;34mA multiplicação entre {num1} x {num2} = {resposta}\033[m')
    elif opção == 3:
        if num1 > num2:
            print(f'\033[1;34mO número {num1} é MAIOR que {num2}\033[m')
        if num2 > num1:
            print(f'\033[1;34mO número {num2} é MAIOR que {num1}\033[m')
    elif opção == 4:
        print('\033[1;33mDigite os novos números!\033[m')
        novo1 = int(input('\033[1;34mPrimeiro número: '))
        novo2 = int(input('Segundo número: \033[m'))
    elif opção == 5:
        print('\033[1;35m SAINDO DO PROGRAMA... \033[m')
        sleep(2)
    else:
        print('\033[1;31m OPÇÃO INVÁLIDA! TENTE NOVAMENTE! \033[m')
print('-=-'*20)
print('\033[1;34mFIM DO PROGRAMA! VOLTE SEMPRE!\033[m')