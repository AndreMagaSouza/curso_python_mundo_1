tipoTemp = int(input("Escolha qual a temperatura de sua região:\n"
                     "1 - Celsius\n"
                     "2 - Fahrenheit\n"
                     "-> "))

if (tipoTemp == 1):
    c = float(input('Digite a temperatura em °C: '))
    f = (c * 1.8) + 32
    print('A temperatura de {:.2f}°C equivalem a {:.2f}°F.'.format(c, f))
elif (tipoTemp == 2):
    f = float(input('Digite a temperatura em °F: '))
    c = (f - 32) / 1.8
    print('A temperatura de {:.2f}°F equivalem a {:.2f}°C.'.format(f, c))
else:
    print("Comando inválido. Tente novamente!")
