# Calcula o valor da prestação.
print(' ====== Exercicio 36 ====== ')

# Recebendo dados.
vc = float(input('Digite o valor da casa: R$'))
sal = float(input('Digite seu salario: R$'))
pres = int(input('Digite em quantos anos vai pagar: '))

# Calculando o valor da PARCELA MENSAL (pm) e 30% do salario.
pm = vc / (pres * 12)
maximo = sal * 30 / 100

# Verificando se o valor da parcela corresponde a no maximo 30% do salario.
if (pm <= maximo):
    print('\nSeu empréstimo foi aprovado!\nO valor da parcela mensal será de: R${:.2f}'.format(pm))
else:
    print('\nSeu empréstimo foi negado!\nO valor da parcela mensal ultrapassa 30% do seu salario!')

