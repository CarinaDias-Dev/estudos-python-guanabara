#Desenvolva um programa que mostre 6 números inteiros e mostre a soma
#apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o#
soma = 0
cont = 0
for c in range(1,7):
    num = int(input(f'Digite o {c} valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você informou {cont} números pares. E a soma foi {soma}')

