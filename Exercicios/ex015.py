d = int(input('Quantos dias ficou com o carro? '))
k = float(input('Quantos km andou? '))
pago = (60 * d) + (k * 0.15)
print('Você ficou {} dias com o carro e percorreu {}km. O total do aluguel é de R${:.2f}.'.format(d, k, pago))

