#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.

vel = int(input('Qual a velocidade atual do seu carro? '))

if (vel > 80):
    multa = float((vel - 80) * 7)
    print('MULTADO! Você ultrapassou o limite de 80km/h.\n'
          'Você deve pagar uma multa de R${:.2f}!\n'
          'Dirija com segurança!' .format(multa))
else:
    print('Tenha um ótimo dia! Dirija com segurança.')
