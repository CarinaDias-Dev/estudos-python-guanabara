#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços#
#exemplos: apos a sopa / a sacada da casa / a torre da derrota / o lobo ama o bolo / anotaram a data da maratona
from operator import invert

frase = str(input('Digite a frase: ')).strip().upper()
separado = frase.split()
junto = ''.join(separado)
inverso = ''
'''inverso = junto[::-1]''' #nesse caso não seria necessaŕio o -for- de repetição
print(f'Você digitou {frase}')
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(f'O INVERSO de {junto} é {inverso}')
if junto == inverso:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase que você digitou NãO é um PALÍNDROMO.')
