salario = float(input('Qual o salário? R$'))
novo = salario+(salario*15/100)
print('O salário R${:.2f} terá um aumento de 15%. Passando a ser R${:.2f}'.format(salario, novo))
