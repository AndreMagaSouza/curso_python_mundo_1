n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
codigo = int(input('Digite a opção do código: 1 ou 2? '))

if (codigo == 1):
    if (n1 > n2 and n1 > n3):
        print('O maior valor digitado foi {}' .format(n1))
    if (n2 > n3 and n2 > n1):
        print('O maior valor digitado foi {}' .format(n2))
    if (n3 > n2 and n3 > n1):
        print('O maior valor digitado foi {}' .format(n3))
    if (n2 > n1 and n3 > n1):
        print('O menor valor digitado foi {}' .format(n1))
    if (n1 > n2 and n3 > n2):
        print('O menor valor digitado foi {}' .format(n2))
    if (n1 > n3 and n2 > n3):
        print('O menor valor digitado foi {}' .format(n3))
else:
    menor = n1
    if (n2 < n1 and n2 < n3):
        menor = n2
    if (n3 < n1 and n3 < n2):
        menor = n3
    print('O menor valor digitado foi {}' .format(menor))
    maior = n1
    if (n2 > n1 and n2 > n3):
        maior = n2
    if (n3 > n1 and n3 > n2):
        maior = n3
    print('O maior valor digitado foi {}' .format(maior))
