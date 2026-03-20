#Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triâgulo
#será formado: - equilatero: todos os lados são iguais.  - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes
r1 = int(input('Primeiro valor: '))
r2 = int(input('Segundo valor: '))
r3 = int(input('Terceiro valor: '))
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('Os Segmentos acima FORMAM UM TRIÂNGULO! ')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos NÃO FORMAM UM TRIÂNGULO!')