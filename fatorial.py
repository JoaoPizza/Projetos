# primeiramente fazer um método para multiplicar e contar uma quantidade de número inserida
# NÃO COMPLICAR O FÁCIL

num = int(input('Digite seu número: '))
fat = 1


for x in range(1,num+1):
    fat = fat * x

print(fat)

#nesse caso oq acontece aqui é que o 'x' é uma variavel criada somente dentro do loop do for
#então nesse caso to falando dentro dessa váriavel, rode o código esse tanto de vezes aqui
#que nesse caso é entre 1 e o número escolhido pelo usuário + 1 por conta que o for começa em 0