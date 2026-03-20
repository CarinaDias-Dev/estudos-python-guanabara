'''O mesmo professor do desafio anterior quer sortear a ordem de apresentação
de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

import random
from random import shuffle
n1 = str(input('O primeiro aluno: '))
n2 = str(input('O segundo aluno: '))
n3 = str(input('O terceiro aluno: '))
n4 = str(input('O quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de alunos para apresenteção do trabalho será:')
print(lista)
