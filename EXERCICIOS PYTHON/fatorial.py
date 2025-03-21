# primeiramente fazer um método para multiplicar e contar uma quantidade de número inserida
# NÃO COMPLICAR O FÁCIL

num = int(input('Digite seu número: '))
fat = 1


for x in range(1,num+1):
    fat = fat * x
    x = x + 1

print(fat)