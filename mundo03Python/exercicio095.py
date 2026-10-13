#Melhorando o exercício 093.
jogador = dict()
principal = list()
partidas = list()
while True:
    jogador.clear() #limpando o dicionário para receber novos dados.
    partidas.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(0, tot_partidas): #For para registrar quantos gools em cada partida.
        partidas.append(int(input(f'   Quantos gools na {p+1}º partida: ')))
    jogador['gools'] = partidas[:]
    jogador['total'] = sum(partidas)
    principal.append(jogador.copy()) #Adicionando uma cópia do dicionário 'jogador' a lista 'principa'. Método.copy()
    while True: #Criando um loop que não para enquanto o usuário digitar dentro da respota.
        resposta = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if resposta in 'SN':
            break
        else:
            print('ERRO! Digite apenas S ou N.')
    if resposta == 'N':
         break
    
#Saída de dados
print('=~'*30)
print('cód ', end=' ')
for i in jogador.keys(): #Cabeçalho da minha lista de jogadores
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(principal): #Lista de jogadores(principal) e seus respectivos dados.
    print(f'{k:>3} ', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True: #Mais um loop que permite fazer consulta de jogadores específicos
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(principal): #tratamento de erro
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else: #Exibição dos daos do jogador escolhido
        print(f'====Levantamento do jogador  {principal[busca]["nome"]}:')
        for i, g in enumerate(principal[busca]['gools']):
            print(f'    Na {i+1}º partida fez {g} gools.')
    print('-'*40)
print('<<<VOLTE SEMPRE>>>')
