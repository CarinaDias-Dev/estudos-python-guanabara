def factorial(num, show=False):
    """ 
    --> Calcule o Factorial de um número.
    :param num: o número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do Factorial de um número num.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c} ', end='')
            if c > 1:
                print(f'x ', end='')
            else:
                print('= ', end='')
        f *= c
    return f


#print(factorial(5, show=True))
help(factorial)
