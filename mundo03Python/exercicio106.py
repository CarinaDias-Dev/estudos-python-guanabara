from time import sleep
c = ('\033[m',         # 0 - Sem cor
     '\033[0;30;41m',  # 1 - vermelhor
     '\033[0;30;42',   # 2 - verde
     '\033[0;30;43',   # 3 - amarelo
     '\033[0;30;44',   # 4 - azul
     '\033[0;30;45',   # 5 - roxo
     '\033[0;30;46'    # 6 - branco
     );

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg)
    print(c[cor], end='')
    print('~'*tam)
    print(msg)
    print('~'*tam)
    print(c[0], end='')


#Programa Princial
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP ', 2)
    comando = input('Digite um comando ou FIM para SAIR -> ')
    if comando.upper() == 'FIM':
        print(f'Você digitou o comando{comando}')
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!')
