'''Crie um programa que leia o nome de uma pessoa e veja se tem 'silva' no nome'''
nome = str(input('Escreva o seu nome completo: ')).strip()
print('O seu nome tem \033[4;35mSilva\033[m? \033[1;36m{}'.format('silva'in nome.lower()))
