pessoa = dict()
todos = list()
total = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['idade'] = int(input(f'Idade: '))
    total += pessoa['idade']
    while True: #Enquanto 'M ou F não estiver em pessoa['sexo'], continua perguntando.
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0] #Usei o [0] para pegar apenas a primeira letra.
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.') #Mensagem de erro para alertar o usuário que o dado inserido está errado.
    todos.append(pessoa.copy()) #Adicionando a minha lista 'todos' uma copia de pessoa.
    while True: #De modo semelhantemente feito na chave 'sexo', coloquei um 'while' para forçar o usuário a digitar a informação correta. Juntamente com a condicional 'if'.
        resposta = str(input('Deseja continuar? [S/N] ')).upper()[0] 
        if resposta in 'NS':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta == 'N':
        break
print('=-'*30)
print(f' A) Foram cadastradas {len(todos)} pessoas')
media = total / len(todos) #Calculando a média usando o método 'len()' para facilitar.
print(f' B) A média de idade é {media:5.2f} anos.')
#Usando um 'for' para encontrar todas as mulheres cadastradas na lista, juntamente com condicional 'if'.
print(' C) As mulheres cadastradas foram: ', end='')
for p in todos:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' - ')
print()
print(' D) Listas das pessoas que estão acima da média: ')
for p  in todos:
    if p['idade'] >= media:
        print(f'{p["nome"]}', end=' - ')
print()
print('<<<<FIM DO PROGRAMA>>>>')
