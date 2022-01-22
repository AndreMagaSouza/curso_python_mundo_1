# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

l1 = float(input('Pode ser um triângulo?\n'
                 '======================\n'
                 'Primeiro lado: '))
l2 = float(input('Segundo lado: '))
l3 = float(input('Terceiro lado: '))

if (l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1):
    print('\033[0;30;42mOs tamanhos informados podem formar um triângulo!\033[m')
else:
    print('\033[7;0;41mOs tamanhos informados não podem formar um triângulo!\033[m')

