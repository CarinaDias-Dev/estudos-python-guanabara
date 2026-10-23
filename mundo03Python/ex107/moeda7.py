def metade(preço):
    """
    -> Definir metade de um valor.
    :param preço: valor a ser calculado.
    return retorna com a metade do valor apresentado. 
    """
    resultado = preço / 2
    return f'{resultado:.2f}'


def dobro(preço):
    """
    -> Definir dobro de um valor.
    :param preço: Valor a ser calculado.
    :return: Retorna com o dobro do valor apresentado. 
    """
    resultado = preço * 2
    return f'{resultado:.2f}'


def aumentar(preço, taxa):
    """
    -> Definir aumento de um valor pelo percentual definido.
    :param preço: valor a ser calculado.
    :param taxa: O percentual definido para o calculo.
    :return: retorna o preço com aumento conforme taxa apresentada. 
    """
    resultado = preço + (preço * taxa / 100)
    return f'{resultado:.2f}'


def diminuir(preço, taxa):
    """
    -> Definir desconto de um valor pelo percentual definido.
    :param preço: valor a ser calculado.
    :param taxa: O percentual definido para o calculo.
    :return: retorna opreço com desconto conforme taxa apresentada. 
    """
    resultado = preço - (preço * taxa / 100)
    return f'{resultado:.2f}'