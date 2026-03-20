#Escreva um programa que pergunte o salário de um funcionário e calcule o valordo seu aumento.
#Para salário superior a R$1250, calcule um aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%
salario = float(input('Digite o valor do seu salário para saber o aumento: R$'))
if salario>=1250:
    aumento = (salario*10/100)+salario
else:
    aumento = (salario*15/100)+salario
print('O salário com aumento vai para \033[1;32mR${:.2f}\033[m'.format(aumento))

