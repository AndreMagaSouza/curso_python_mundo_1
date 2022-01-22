lar = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))

metQuad = lar * alt
tinta = metQuad/2

print("Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {}m².\n"
      "Para pintar essa parede, você precisará de {}l de tinta.".format(lar, alt, metQuad, tinta))
