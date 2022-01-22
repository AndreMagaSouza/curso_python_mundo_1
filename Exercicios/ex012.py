pp = float(input("Qual é o preço do produto? R$"))
desc = int(input("Qual é o valor do desconto? "))
novo = pp - (pp * desc / 100)

print("O produto que custava R${:.2f}, na promoção com desconto de {}% vai custar R${:.2f}." .format(pp, desc, novo))
