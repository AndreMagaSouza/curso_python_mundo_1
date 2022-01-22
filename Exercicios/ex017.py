from math import hypot
op = float(input('Digite o tamanho do cateto oposto: '))
ad = float(input('Digite o tamanho do cateto adjacente: '))
print('A hipotenusa é {:.2f}.'.format(hypot(op, ad)))
