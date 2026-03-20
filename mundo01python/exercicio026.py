'''Crie um programa que leia uma frase e diga quantas vezes aparece a letras 'a'
em quais posições ela aparece na primeira vez e na ultima'''
frase = str(input('Escreva uma frase: ')).lower().strip()
print('A letra A aparece {} vezes'.format(frase.count('a')))#vai contar quantas vezes aparece algo
print('A \033[1;34mletra A \033[maparece na posição \033[1;34m{}\033[m pela primeira vez'.format(frase.find('a')))
print('E na \033[1;34mposição {}\033[m pela ultima vez'.format(frase.rfind('a')))
