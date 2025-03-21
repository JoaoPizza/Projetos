#projeto calculadora


def calc():
    num = float(input('Digite o primeiro número: '))
    núm2 = float(input('Digite o segundo número: '))
    op = str(input('Digite qual operação você deseja (+, -, *, /): '))
    if op == '+':
        som = float(num + núm2)
        print('A sua soma de {} + {} é igual a {}'.format(num, núm2, som))
    elif op == '-':
        dim = float(num - núm2)
        print('A sua subtração de {} - {} é igual a {}'.format(num, núm2, dim))
    elif op == '*':
        mul = float(num * núm2)
        print('A multiplicação de {} * {} é {}'.format(num, núm2, mul))
    elif op == '/':
        div = float(num / núm2)
        print('A sua divisão de {} / {} é {}'.format(num, núm2, div))

calc()