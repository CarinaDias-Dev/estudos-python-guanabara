#Criei uma lista vazia.
lista = list()
#usei o comando 'for' para definir  tamanho da minha lista e fazer a inserção dos elementos na lista.
for p in range(0, 5):
    print('-='*20)
    elemento = int(input("Insira um número na sua lista: ")) #input para a entrada de dados a minha lista.
    if p == 0 or elemento > lista[-1]:  #condição: se o elemento for o primeiro ou se o elemento for maior que o elemento que está na ultima posição, ele será incluido ao final da lista.
        lista.append(elemento)
        print('Adicionado ao final da lista...')
    else: # se não, será feita uma verificação dos valores dos elementos e sua posição utilizando o comando while. 
        posicao = 0
        while posicao < len(lista): #O comando len() informa o tamanho da minha lista.
            if elemento <= lista[posicao]: #Se o elemento for maior ou igual ao que esta na posição indicada, então será feita a inserção deste elemento na posição através do comando insert(posição, elemento)
                lista.insert(posicao, elemento)
                print(f'Adicionado na posição {posicao} da lista...')
                break
            posicao += 1
print('-='*20)
print(f'Os elementos da lista são: {lista}')
