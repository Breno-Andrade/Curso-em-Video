print(' ====== Exercicio 23 ====== ')

num = str(input('informe um numero: ')).strip()
print('Unidade: {}'.format(num[len(num) - 1: len(num)]))
print('Dezena: {}'.format(num[len(num) - 2: len(num) - 1]))
print('Centena: {}'.format(num[len(num) - 3: len(num) - 2]))
print('Milhar: {}'.format(num[len(num) - 4: len(num) - 3]))
