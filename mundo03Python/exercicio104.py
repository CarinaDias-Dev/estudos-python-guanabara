def leiaInt(msg:str):
    while True:
        valor = input(msg)
        if valor.isnumeric():
            return int(valor)
        else:
            print('\033[31mERRO! Digite um inteiro válido\033[m')


print('-'*20)
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
