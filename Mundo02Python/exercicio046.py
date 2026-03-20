#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos
#de artifícios, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
print('='*50)
print('JÁ VAI COMEÇAR A CONTAGEM REGRECIVA PARA OS FOGOS!')
print('='*50)
sleep(3)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[1;34mFELIZ ANO NOVO!')


