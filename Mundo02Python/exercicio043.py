#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
# e mostre seu status, de acordo com a tabela abaixo:
#Abaixo de 18.5: Abaixo do peso   - 25 até 30: Sobrepeso
#Entre  18.5 e 25: Peso ideal     - 30 até 40: Obesidade   - Acima de 40: Obesidade mórbida
peso = float(input('Digite seu peso (kg) '))
altura = float(input('Digite sua altura (m) '))
imc = peso / (altura * altura)
print(f'O seu IMC é {imc:.1f}.')
if imc < 18.5:
    print('ABAIXO DO PESO.')
elif 18.5 <= imc < 25:
    print('PESO IDEAL!')
elif 25 <= imc < 30:
    print('SOBREPESO!')
elif 30 <= imc < 40:
    print('OBESSIDADE!')
else:
    print('OBESSIDADE MÓRBIDA, CUIDADO!')
