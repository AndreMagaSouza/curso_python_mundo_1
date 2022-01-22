# Desafio 005
x = int(input('Digite um número: '))
print('O sucessor de {} é {} e o seu antecessor é {}.'.format(x, x+1, x-1))

# Desafio 006
x = int(input('Digite um número: '))
print('O dobro de {} é {}, o triplo é {} e sua raiz quadrada é {}.'.format(x, x*2, x*3, x**(1/2)))

# Desafio 007
n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A primeira nota foi {} e a segunda {}. A média entre elas é {}.'.format(n1, n2, m))

# Desafio 008
met = float(input('Digite uma metragem: '))
cm = met*100
ml = met*1000
print('{} metros tem {} cm e {} milímetros.'.format(met, cm, ml))

# Desafio 009
n = int(input('Digite um número: '))
i = 0
while i <= 10:
    print('{} x {} = {}'.format(n, i, n*i))
    i += 1

# Desafio 010
r = float(input('Quantos reais você tem? '))
d = r / 3.27
print('Com {} reais você pode comprar {:.2f} dólares.'.format(r, d))

# Desafio 011
L = float(input('Qual a largura da parede? '))
h = float(input('Qual a altura da parede? '))
area = L * h
t = area / 2
print('Sua parede tem {} m². Para pintá-la serão necessários {} litros de tinta.'.format(area, t))

# Desafio 012
p = float(input('Digite o valor do produto: '))
d = p - (p * 5 / 100)
print('Com nosso desconto de 5%, o seu produto era {} reais e passou a ser {:.2f} reais.'.format(p, d))

# Desafio 013
s = float(input('Digite seu salário: '))
ns = s + (s * 15/100)
print('Seu salário atual é R${:.2f}. Com sua promoção o seu salário vai passar a ser R${:.2f}.'.format(s, ns))
