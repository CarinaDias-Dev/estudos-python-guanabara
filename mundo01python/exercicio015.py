dias = int(input('Quantos dias será alugado: '))
quilometros = float(input('Quantos quilômetros foram percorridos? '))
dia = dias*60
km = quilometros*0.15
print('O total a pagar é : R${:.2f}'.format((dia+km)))
