def voto(ano):
    from datetime import date #importe a biblioteca dentro da função, quando ele for usada apenas nela, para econimizar espaço na memória.
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com idade {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com idade {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com idade {idade} anos: VOTO OBRIGATÓRIO.'


nasc = int(input('Qual o ano do nascimento: '))
print(voto(nasc))
