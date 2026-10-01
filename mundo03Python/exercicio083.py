expressao = input('Digite a expressão: ') #O usuário entra com a expressão.
lista = [] #Lista criada para armazenar e relacionar os parágrafos que estiverem na expressão.
for elemento in expressao:
    if elemento == '(': #Se entrou um parágrafo abrindo, ele será incluído na lista.
        lista.append('(')
    elif elemento == ')': #Se entrou um parenteses fechando será verificado se a lista esta cheia, se sim será removido um parágrafo de abertura.
        if len(lista) > 0:
            lista.pop()
        else: #Se a lista estiver vazia quando tiver um ')' quer dizer que existe um parágrafo sobresalente e então será incluido na lista a fim de indicar que esse não achou o seu par.
            lista.append(')')
            break
#Verificação final. Se a lista estiver vazia é sinal de que todos os '(' encontraram o seu par ')'. Concluimos então que a expressão é válida. Caso contrário, a expressão é considerada inválida.
if len(lista) == 0:
    print('Sua expressão esta válida.')
else:
    print('Sua expressão esta inválida.')
