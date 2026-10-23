def metade(preço=0, formatar=False):
    """
    -> Definir metade de um valor.
    :param preço: valor para calcular.
    :param formatar: valor opcional, indicando se deve ou não adicionar formatação ao valor. (ex.: R$0000,00)
    return retorna com o dobro do valor apresentado. 
    """
    resultado = preço / 2
    return resultado if formatar is False else moeda(resultado)


def dobro(preço=0, formatar=False):
    """
    -> Definir dobro de um valor.
    :param preço: Valor a ser calculado.
    :param formatar: valor opcional, indicando se deve ou não adicionar formatação ao valor. (ex.: R$0000,00)
    :return: Retorna com o dobro do valor apresentado. 
    """
    resultado = preço * 2
    return resultado if formatar is False else moeda(resultado)


def aumentar(preço=0, taxa=0, formatar=False):
    """
    -> Definir aumento de um valor pelo percentual definido.
    :param preço: valor a ser calculado.
    :param taxa: O percentual definido para o calculo.
    :param formatar: valor opcional, indicando se deve ou não adicionar formatação ao valor. (ex.: R$0000,00)
    :return: retorna o preço com aumento conforme taxa apresentada. 
    """
    resultado = preço + (preço * taxa / 100)
    return resultado if not formatar else moeda(resultado)


def diminuir(preço=0, taxa=0, formatar=False):
    """
    -> Definir desconto de um valor pelo percentual definido.
    :param preço: valor a ser calculado.
    :param taxa: O percentual definido para o calculo.
    :param formatar: valor opcional, indicando se deve ou não adicionar formatação ao valor. (ex.: R$0000,00)
    :return: retorna o preço com desconto conforme taxa apresentada. 
    """
    resultado = preço - (preço * taxa / 100)
    return resultado if not formatar else moeda(resultado)


def moeda(preço=0, moeda='R$'):
    """
    -> Define a formatação de uma moeda (ex.: R$0000,00).
    :param preço: valor a ser formatado.
    :param moeda: Define o sifrão do preço informado.
    :return: Retorna com o preço formatado. 
    """
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=10, taxar=15):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de desconto: \t{diminuir(preço, taxar, True)}')
    print('-'*30)
    