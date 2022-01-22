p = float(input("Qual o valor do produto? R$"))
pag = int(input("A forma de pagamento vai ser:\n1 - à visa\n2 - parcelado até 5x\n-> "))
vist = p - (p * 10 / 100)

if (pag == 1):
    print("Com o pagamento à vista você tem 10% de desconto. O novo valor é de R${:.2f}." .format(vist))
elif (pag == 2):
    x = int(input("Quantas parcelas? "))
    if (x == 2):
        print("Dividindo em {}x você recebe o desconto de 5%. O novo valor é de R${:.2f}." .format(x, (p-(p*5/100))))
    elif (x == 3):
        print("Dividindo em {}x você recebe o desconto de 4%. O novo valor é de R${:.2f}.".format(x, (p-(p*4/100))))
    elif (x == 4):
        print("Dividindo em {}x você recebe o desconto de 3%. O novo valor é de R${:.2f}.".format(x, (p-(p*3/100))))
    elif (x == 5):
        print("Dividindo em {}x você recebe o desconto de 2%. O novo valor é de R${:.2f}.".format(x, (p-(p*2/100))))
    else:
        print("Opção inválida. Tente novamente!")
else:
    print("Opção inválida. Tente novamente!")
