print(' ====== Exercício 10 ====== ')
# Atribuindo o valor digitado pelo usuário a uma variavel.
r = float(input('Quanto voce tem na carteira ? R$: '))
# Dividindo o valor inserido pelo usuário pelo valor do dólar no dia 19/07/2021
d = r / 5.25
# Exibindo o resultado para o usuário.
print('Com {:.2f} voce pode comprar U${:.2f}'.format(r, d))
