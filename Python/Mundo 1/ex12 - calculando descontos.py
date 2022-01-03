print(' ====== Exercício 12 ====== ')
# Solicitado o valor para o usuário.
preço = float(input('Qual o valor do produto? R$'))
# Calculando o valor inserido pelo usuário com 5% de desconto.
novo = preço - (preço * 5 / 100)
# Exibindo o resultado para o usuário.
print(' o produto que custava {}, na promoção com 5% de desconto custara R${:.2f}'.format(preço, novo))
