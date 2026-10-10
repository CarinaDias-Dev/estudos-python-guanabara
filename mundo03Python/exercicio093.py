jogador = dict() #dicionário para guardar todas as informações necessárias
partidas = list() #lista para armazenar a quantidade de gools em cada partida.
jogador['nome'] = str(input('Nome do jogador: '))
tot_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? ')) #variável para o total de partidas.
for p in range(0, tot_partidas): #Registrando a quantidade de gools para cada partida.
    partidas.append(int(input(f'Quantos gools na {p+1} partida? ')))
jogador['gools'] = partidas[:] #criando a chave gools dentro do dicionário 'jogadores', com uma cópia da lista 'partidas'.
jogador['tot_gools'] = sum(partidas) #Metodo 'sum()' serve para somar (neste caso somando partidas).
#Exibição do resultado de três maneiras diferentes a seguir.
print('-'*30)
print(jogador)
print('-'*30)
for k, v in jogador.items(): #Metodo 'items()' para exibir todos os elementos dentro do dicionário. Tanto a chave (key) quanto o valor (values).
    print(f'O campo {k} é igual a {v}')
print('='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gools"])} partidas') #Usando método len() para obter o total de partidas.
for i, v in enumerate(jogador['gools']): #Usando o 'enumerate()' para vasculhar uma lista expecifica (gools). Também é capaz de me dar o indice e o valor.
    print(f'    => Na partida {i+1} fez {v} gools.')
print(f'Foi o total de {jogador["tot_gools"]} gools')
