'''Faça um programa que leia o nome de uma pessoa e mostre em seguida o primeiro nome
e o último nome separadamente. ex: Ana Maria De Souza primeiro=Ana ultimo=Souza'''
nome = str(input('Digite o seu nome: ')).strip()
n = nome.split()#SPIT VAI DIVIDIR O TEXTO
print('Prazer em te conhecer! {}'.format(nome))
print('O seu primeiro nome é {}'.format(n[0]))
print('O último nome é {}'.format(n[len(n)-1]))#len vai encontrar. no caso -1 é o ultimo, -2 o penultimo...
