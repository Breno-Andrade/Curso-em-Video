from random import randint
from  time import sleep

# O clássico jogo do pedra papel e tesoura.
opções = ['Pedra', 'Papel', 'Tesoura']
maquina = randint(0, 2)

print(' ====== Exercicio 45 ====== ')

# Opções validas
print('''
Escolhas Disponíveis
====================
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
====================
''')

# Escolha do usuário
usuário = int(input('Faça sua escolha: '))

# Fazendo exibição pausada
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!\n')

# Verificando se a opção escolhida pelo usuário é valida.
if usuário >= 0 and usuário <= 2:
    print('=' * 30)
    print('Computador jogou {}!'.format(opções[maquina]))
    print('Jogador jogou {}!'.format(opções[usuário]))
    print('=' * 30)

    print('\nResultado do Jogo: ', end = '')
    
    # Verificando o ganhador do jogo.
    if usuário == 0:
        if maquina == 2:
            print('Você venceu, terei mais sorte na proxima!')
        elif maquina == 1:
            print('Vitoria da maquina! Mais sorte na proxima!')
        else:
            print('Empatamos, mas tenho certeza de que vencerei na proxima!')
    elif usuário == 1:
        if maquina == 0:
                print('Você venceu! terei mais sorte na proxima!')
        elif maquina == 2:
                print('Vitoria da maquina! Mais sorte na proxima!')
        else:
            print('Empatamos, mas tenho certeza de que vencerei na proxima!')
    elif usuário == 2:
        if maquina == 1:
            print('Você venceu, terei mais sorte na proxima!')
        elif maquina == 0:
            print('Vitoria da maquina! Mais sorte na proxima!')
        else:
            print('Empatamos, mas tenho certeza de que vencerei na proxima!')
else:
    print('Jogador jogou Opção Invalida!')
    print('=' * 30)
    print('\nResultado do Jogo: Vitoria da maquina! Escolha uma opção valida na próxima!!')
