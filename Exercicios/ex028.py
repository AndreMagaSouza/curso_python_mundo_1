from random import randint
from time import sleep

print('-=' * 27)
print('Vou pensar em um número entre 0 e 5. Adivinhe qual é!')
print('-=' * 27)
n1 = int(input('Em que número eu pensei? '))
x = randint(0, 5)
print('PROCESSANDO.....')
sleep(1.5)
if (n1 == x):
    print('PARABÉNS! Eu pensei em {} e você escolheu {}.' .format(x, n1))
else:
    print('GANHEI! Eu pensei no número {} e não {}.' . format(x, n1))