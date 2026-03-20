velocidade = float(input('Qual a velocidade do carro? '))
multa = (velocidade - 80)*7
if velocidade > 80:
    print('\033[1;31mMULTADO!\033[m Você excedeu o limite de velocidade permitido que é de \033[1;30;41m80Km/h\033[m')
    print('Você deverá pagar uma \033[1;31mmulta\033[m no valor de \033[1;33mR${:.2f}\033[m'.format(multa))
else:
    print('Você esta dentro do limite de velocidade! \033[1;33mNão ultrapasse o limite!\033[m')
print('Tenha um \033[1;36mBOM DIA!\033[m Dirija com segurança!')