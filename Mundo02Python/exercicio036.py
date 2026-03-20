#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa,o salário do comprador e em quantos anos ele vai pagar.
#calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado.

casa = float(input('Qual o valor da casa R$'))
salario = float(input('Qual o salário do comprador? R$'))
anos = int(input('Em quantos anos você deseja pagar o emprestimo? '))
minimo = salario*30 / 100
prestacao = casa / (anos*12)
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa,anos))
print('A prestação será de R${:.2f}'.format(prestacao))
if prestacao<= minimo:
    print('EMPRESTIMO APROVADO!')
else:
    print('EMPRESTIMO NEGADO!')
    print('A prestação excedeu á 30% do salário informado.')