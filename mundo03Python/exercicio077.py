#criei uma tupla 'palavras'
palavras = ('aprender', 'programar', 'liguagem',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
#criei um laço para cada palavra em palavras
print(len(palavras))
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ',end='')
    #criei mais um laço para vasculhar as letras em cada palavra. E um 'if' para achar vogais em cada palavra
    for letra in p:
        if letra.lower() in 'aeiou':  #colocando as letras em minusculas e procurando as vogais
            print(letra, end=' ')
