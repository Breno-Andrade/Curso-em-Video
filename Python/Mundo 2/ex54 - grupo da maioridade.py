from datetime import date
print(' ====== Exercicio 54 ====== ')

data = date.today().year
maior = 0
menor = 0

for i in range(1, 8):
    nasc = int(input('Digite o ano de nascimento da {}° pessoa: '.format(i)))
    idade = data - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print('\nDas pessoas inseridas, {} ja fazem parte da maioridade e {} são menores de idade!!'.format(maior, menor))

