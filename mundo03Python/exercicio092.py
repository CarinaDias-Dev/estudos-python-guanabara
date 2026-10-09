from datetime import datetime
pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
nasc = int(input('Ano do Nascimento: '))
pessoa['idade'] = datetime.now().year - nasc
pessoa['ctps'] = int(input('Carteira de trabalho (0 se não tiver) '))
if pessoa['ctps'] != 0:
    pessoa['ano_contrato'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['ano_contrato'] + 35) - datetime.now().year)
print('=-'*30)
for k, v in pessoa.items():
    print(f'   -{k} tem valor {v}')
    