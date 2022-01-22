import random

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
rand = random.choice([n1, n2, n3, n4])
print('O aluno(a) escolhido(a) foi: {}' .format(rand))
