def metade(preço=0):
    """
    -> Definir metade de um valor.
    :param preço: valor a ser calculado.
    return retorna com a metade do valor apresentado. 
    """
    resultado = preço / 2
    return f'{resultado:.2f}'


def dobro(preço=0):
    """
    -> Definir dobro de um valor.
    :param preço: Valor a ser calculado.
    :return: Retorna com o dobro do valor apresentado. 
    """
    resultado = preço * 2
    return f'{resultado:.2f}'


def aumentar(preço=0, taxa=0):
    """
    -> Definir aumento de um valor pelo percentual definido.
    :param preço: valor a ser calculado.
    :param taxa: O percentual definido para o calculo.
    :return: retorna o preço com aumento conforme taxa apresentada. 
    """
    resultado = preço + (preço * taxa / 100)
    return f'{resultado:.2f}'


def diminuir(preço=0, taxa=0):
    """
    -> Definir desconto de um valor pelo percentual definido.
    :param preço: valor a ser calculado.
    :param taxa: O percentual definido para o calculo.
    :return: retorna o preço com desconto conforme taxa apresentada. 
    """
    resultado = preço - (preço * taxa / 100)
    return f'{resultado:.2f}'


def moeda(preço=0, moeda='R$'):
    """
    -> Define a formatação de uma moeda (ex.: R$0000,00).
    :param preço: valor a ser formatado.
    :param moeda: Define o sifrão do preço informado.
    :return: Retorna com o preço formatado. 
    """
    return f'{moeda}{preço}'.replace('.', ',')
