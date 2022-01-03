print(' ====== Exercicio 51 ====== ')

# Primeiro Termo.
pt = int(input('Digite o primeiro termo: '))
# Razão.
rz = int(input('Digite a razão: '))
# Décimo Termo.
dt = pt + (10 - 1) * rz

# Exibe a progressão aritmética.
for c in range (pt, dt + rz, rz):
    print('{}'.format(c), end = ' -> ')
print('ACABOU')
