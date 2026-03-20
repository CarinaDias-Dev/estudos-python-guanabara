#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor:'))
#verificar o menor valor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#verificar o maior valor
maior = b
if a>b and a>c:
    maior = a
if c>a and c>b:
    maior = c
print('O menor valor é \033[33m{}\033[m'.format(menor))
print('O maior valor é \033[34m{}\033[m'.format(maior))
