pessoa = []
galera = []
while True:
    nome = pessoa.append(input('Informe o nome: '))
    peso = pessoa.append(float(input('Informe o peso(kg): ')))
    galera.append(pessoa[:])
    pessoa.clear()
    resposta = input('Deseja continuar? [S/N] ').upper()
    if resposta in 'N':
        break
print('=='*20)
print(f'{'LISTA DE PESSOAS CADASTRADAS':^40}')
print('=='*20)
for d in galera:
        print(f'Nome: {d[0]:<10} Peso: {d[1]:>3}Kg')
print('=='*30)
print(f'Foram cadastradas {len(galera)} pessoas')
mais_pesado = []
menos_pesado = []
for p in galera:
     if p[1] < 90:
          menos_pesado.append(p)
     else:
          mais_pesado.append(p)
print(f'As pessoas mais pesada foram {mais_pesado}')
print(f'As pessoas mais leves são: {menos_pesado}')
print('=='*60)