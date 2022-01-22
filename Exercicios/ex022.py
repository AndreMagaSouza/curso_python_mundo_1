
# CONTINUAR CONTINUAR CONTINUAR CONTINUAR CONTINUAR CONTINUAR CONTINUAR

nome = input('Digite o seu nome completo: ').strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}' .format(nome.upper()))
print('Seu nome me minúsculas é {}' .format(nome.lower()))
print('Seu nome tem ao todo {} letras' .format(len(nome)-nome.count(' ')))

lista = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras' .format(lista[0], len(lista[0])))
