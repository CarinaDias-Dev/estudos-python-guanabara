#crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
# pessoas não atingiram a maior idade e quantas já são maiores.#
from datetime import date

atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nascimento = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    idade = atual - nascimento
    if idade >= 21:
        totmaior += 1
    elif idade < 21:
        totmenor += 1
print(f'O total são {totmaior} pessoas maiores de idade. \nE {totmenor} pessoas menores.')
