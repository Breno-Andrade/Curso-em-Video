print(' ====== Exercicio 50 ====== ')
s = 0
for i in range(0, 6):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        s += n
print('Resultado da soma dos pares inseridos: {}'.format(s))