#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade,
#se ele ainda vai se alistar ao serviço militar, se esta na hora de se alistar ou se já passou o tempo
#do alistamento. Seu programa deverá mostrar o tempo que falta ou que passou o prazo.
from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano do seu nascimento: '))
idade = atual -nascimento
print(f'Você nasceu em \033[1;34m{nascimento}\033[m e tem \033[1;34m{idade}\033[m anos de idade em \033[1;34m{atual}\033[m.')
if idade == 18:
    print('Você deve se alistar imediatamente!')
elif idade > 18:
    ano = nascimento + 18
    tempo = idade - 18
    print('O tempo para o seu alistamento obrigatório já passou.')
    print(f'o ano do seu alistamneto foi {ano}')
    print(f'Se passaram {tempo} anos.')
elif idade < 18:
    ano = nascimento + 18
    tempo = 18 - idade
    print('Você ainda não esta na idade para se alistar.')
    print(f'O ano do seu alistamento será {ano}')
    print(f'faltam {tempo} anos para o seu alistamento obrigatório')