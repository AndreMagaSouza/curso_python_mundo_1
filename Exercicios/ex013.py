sal = float(input("Qual é o salário do funcionário? R$"))
aum = int(input("Qual o aumento em porcentagem? "))
reaj = sal + (sal * aum / 100)

print("O funcionário ganhava R${:.2f}. Com o aumento de {}% vai passar a receber R${:.2f}." .format(sal, aum, reaj))

