#A confederação nascional de natação precisa de um programa que leia o ano de
#nascimento de um atleta e mostre a sua categoria de acordo com a idade:
# até 9 anos: mirim   - até 14 anos: infantil  - Até 19 anos: junior  - ate 25 anos sênior
#acima: master
from datetime import date

atual = date.today().year
nascimento = int(input('Digite o ano do seu nascimento: '))
idade = atual - nascimento
print(f'O atleta nasceu em {nascimento} e sua idade é {idade} anos em {atual}')
if idade <= 9:
    print('Você faz parte da categoria MIRIM.')
elif 9 < idade <= 14:
    print('Você faz parte da categoria INFANTIL.')
elif 14 < idade <=19:
    print('Você faz parte da categoria JUNIOR')
elif 19 < idade <=25:
    print('Você faz parte da categoria SÊNIOR')
else:
    print('Você faz parte da categoria MASTER')
