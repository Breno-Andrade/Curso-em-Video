print(' ====== Exercício 49 ====== ')

# Inserindo o valor digitado pelo usuário à uma variavel.
num = int(input('Digite um numero para ver sua tabuada: '))

print('=' * 15)
for i in range(0, 11):
    print('{} x {} = {}'. format(num, i, num * i))
print('=' * 15)
