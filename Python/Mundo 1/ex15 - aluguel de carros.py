print(' ====== Exercício 15 ====== ')
# Entrada de dados.
dias = int(input('Quantos Dias alugados? '))
km = float(input('Quantos Km rodados? '))
# Calculado o valor a pagar (processamento de dados).
total = (dias * 60) + (km * 0.15)
print('O total a pagar é:R${:.2f}'.format(total))
