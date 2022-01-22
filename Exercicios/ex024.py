cidade = input('Em que cidade você nasceu? ').strip()
lista = cidade.split()
nome = lista[0].lower()
print(nome == 'santo' or nome == 'santos' or nome == 'santa')

# Outra forma de fazer

cid = input('Qual cidade você nasceu? ').strip()
print(cid[:5].lower() == 'santo' or cid[:6].lower() == 'santos' or cid[:5].lower() == 'santa')
