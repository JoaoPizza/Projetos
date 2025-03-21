# a=pi*r²

print('Bem vindo a sua calculadora de área de uma circunferência!')

raio = float(input('Digite aqui o raio da sua circunferência: '))
pi = 3.14
quad = raio ** 2
area = pi * quad

print('A área da sua circunferência é: {:.2f}m²'.format(area))
