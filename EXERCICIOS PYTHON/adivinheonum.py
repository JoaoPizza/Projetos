'''
palpite = int(input('Digite o seu palpite: '))
num = 6

while palpite != num:
    nov = int(input('Você errou! Tente novamente: '))
    palpite = nov
else:
    print('Parabéns, você acertou!')
'''

palpite = 0
num = 6


while True:
    palpite = int(input('Digite seu palpite: '))
    if palpite == num:
        print('Parabéns, você acertou!')
        break
    else:
        print('Você errou! Tente novamente')

