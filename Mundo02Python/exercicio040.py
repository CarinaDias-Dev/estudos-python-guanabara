#Crie um programa que leia duas notas de um aluno e calcule sua média.
#Mostrando uma mensagem no final, de acordo com a média atingida:
#média abaixo de 5.0: Reprovado
#média entre 5.0 e 6.9: Recuperação
#média 7.0 ou superior: aprovado

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2) / 2
print(f'A média entre {n1} e {n2} é {media}.')
if media < 5:
    print('Que pena! Você foi REPROVADO.')
elif 7 > media >=5:
    print('Você está de RECUPERAÇÃO.')
elif media > 7:
    print('PARABÉNS! Você foi APROVADO!')
