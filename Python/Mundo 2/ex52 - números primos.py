print(' ====== Exercicio 52 ====== ')

num = int(input('Digite o numero: '))

# Total de vezes que o numero foi divisível.
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        tot += 1
print('\nO número {} foi divisível {} vezes. E por isso ele '.format(num, tot), end = '')
if tot == 2:
    print('É PRIMO!!!')
else:
    print('NÃO É PRIMO!!!')
