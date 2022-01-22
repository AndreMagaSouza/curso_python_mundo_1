rs = float(input("Quanto de dinheiro você tem na carteira? R$"))
conv = float(rs / 5.70)

print("Com R${:.2f} você pode comprar US${:.2f}!" .format(rs, conv))
