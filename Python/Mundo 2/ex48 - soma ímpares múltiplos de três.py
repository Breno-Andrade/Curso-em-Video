s = 0
print(' ====== Exercicio 48 ====== ')
print('Soma impares múltiplos de tres!')

print('O resultado da soma é: ', end = '')
for i in range(1, 501, 2):
    if i % 3 == 0:
        s += i
print(s)