print(' ====== Exercicio 55 ====== ')

# Identifica o maior e o menor da sequencia.
maior = 0
menor = 0

for i in range(0, 5):
    peso = float(input('Insira o peso da {}° pessoa: '.format(i + 1)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O menor peso das pessoas inseridas é: {:.1f}'.format(menor))
print('O menor peso das pessoas inseridas é: {:.1f}'.format(maior))
