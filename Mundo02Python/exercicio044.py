#Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto    - em até 2x no catão: preço normal
# - à vista no cartão: 5% de desconto  - 3x ou mais no cartão: 20% de juros#
print('{:=^40}'.format('LOJAS CARINA'))
produto = float(input('Digite o preço do produto: R$'))
print('=='*20)
print('''Selecione a opção correspondente a forma de pagamento: 
[ 1 ] À vista (dinheiro/cheque)
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
print('=='*30)
pagamento = int(input('DIGITE O NÚMERO DA OPÇÃO CORRESPONDENTE: '))
print('=='*30)
print(f'VALOR DO PRODUTO: R${produto:.2f}')
print('=='*30)
if pagamento == 1:
    total = produto - (produto * 10 / 100)
    print(f'PAGAMENTOS À VISTA (dinheiro/cheque) tem desconto de 10%')
    print(f'Valor do produto com desconto: R${total:.2f}')
elif pagamento == 2:
    total = produto - (produto * 5 / 100)
    print('Pagamento À VISTA NO CARTÃO receberá um desconto de 5% ')
    print(f'Valor do produto com desconto: R${total:.2f}')
elif pagamento == 3:
    parcela = produto / 2
    print(f'2x de R${parcela:.2f} sem juros')
    print(f'Valor tota R${produto:.2f}')
elif pagamento == 4:
    total = produto + (produto * 30 / 100)
    parcela = int(input('Quantas parcelas? '))
    totalparcelas = produto / parcela
    print(f'Serão {parcela}x de R${totalparcelas:.2f} com juros de 30%. ')
else:
    print('OPÇÃO INVALIDA! DIGITE UM NÚMERO VÁLIDO.')
