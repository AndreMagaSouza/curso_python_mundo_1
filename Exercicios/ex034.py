# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Digite o salario do funcionário: R$'))
if (sal > 1250):
    aum = sal + (sal * 10) / 100
    print('O funcionário vai passar a receber R${:.2f}.' .format(aum))
else:
    aum = sal + (sal * 15) / 100
    print('O funcionário vai passar a receber R${:.2f}.' .format(aum))

