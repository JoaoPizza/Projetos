num = int(input('Digite seu número: '))

if num > 1:
    for x in range(2,num):
        if num % x == 0:
            print('Esse não é um número primo!')
            break
    else:
        print('Este é um número primo!')