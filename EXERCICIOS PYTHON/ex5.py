# duas entradas, uma de valor do produto outra de porcentagem de desconto

print('Bem vindo a sua calculadora de descontos!')

val = float(input('Digite o valor original do seu produto: '))
des = float(input('Digite quantos porcento de desconto você terá no produto (somente números): '))
desr = des / 100
fin = val * desr
real = val - fin

print('Na sua compra de um produto que originalmente custaria R${}, com {:.0f}% de desconto você terá um desconto de R${}. Assim sua compra ficará no valor final de R${}'.format(val,des,fin,real))
