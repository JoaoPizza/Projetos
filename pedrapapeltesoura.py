#criar função para a escolha do jogador e escolha da máquina validando resposta com lista

from random import choice

vit_jogador = 0
vit_maquina = 0


def op_jogador():
    esc_jogador = str.lower(input('Escolha entre: Pedra, Papel ou Tesoura: '))
    if esc_jogador == 'papel':
        return esc_jogador
    elif esc_jogador == 'pedra':
        return esc_jogador
    elif esc_jogador == 'tesoura':
        return esc_jogador
    else:
        print('A opção digitada é inválida!')

def op_maquina():
    esc_maquina = choice(['pedra', 'papel', 'tesoura'])
    return esc_maquina

while True:
    print('-'*50)
    esc_jogador = op_jogador()
    print('-'*50)
    esc_maquina = op_maquina()

    if (esc_jogador == 'pedra' and esc_maquina == 'tesoura' \
        or esc_jogador == 'papel' and esc_maquina == 'pedra' \
            or esc_jogador == 'tesoura' and esc_maquina == 'papel'):
        print(f'Jogador escolheu {esc_jogador} e a máquina escolheu {esc_maquina}. Você ganhou!')
        vit_jogador += 1
    elif esc_jogador == esc_maquina:
        print(f'Jogador escolheu {esc_jogador} e a máquina escolheu {esc_maquina}. Empate!')
    else:
        print(f'Jogador escolheu {esc_jogador} e a máquina escolheu {esc_maquina}. Você perdeu!')
        vit_maquina += 1

    print('-'*50)
    print(f'Vitórias jogador: {vit_jogador}. Vitórias máquina: {vit_maquina}.')
    print('-'*50)


    sair = input('Deseja jogar novamente? ')
    if sair in ['Sim', 'sim', 'SIM', 's', 'S']:
        pass
    elif sair in ['Não', 'não', 'NÃO', 'n', 'N']:
        break
    else:
        break