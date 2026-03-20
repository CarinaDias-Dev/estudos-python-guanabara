'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do
seno, coseno e tangente desse ângulo'''

from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que desejar: '))
seno = sin(radians(angulo))
print('_'*20)
print('O ângulo {} tem o SENO {:.2f}'.format(angulo, seno))
coseno = cos(radians(angulo))
print('O COSENO {:.2f}'.format(coseno))
tangente = tan(radians(angulo))
print('A TANGENTE {:.2f}'.format(tangente))
print('_'*20)
