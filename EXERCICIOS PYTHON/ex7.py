# dólar 6,20

print('Bem vindo ao seu conversor de moedas!')

tipo = str.upper(input('Digite a moeda desejada para converter (DOL ou EUR): '))


if tipo == 'DOL':
    dol = 6.20
    moed = float(input('Digite agora a quantidade de reais que deseja converter para a moeda escolhida: R$'))
    conv = moed * dol
    print('R${} convertido em Dólares como escolhido dá um total de ${}.'.format(moed,conv))
elif tipo == 'EUR':
    eur = 6.40
    moed2 = float(input('Digite agora a quantidade de reais que deseja converter para a moeda escolhida: R$'))
    conv2 = moed2 * eur
    print('R${} convertido em Dólares como escolhido dá um total de ${}.'.format(moed2,conv2))