print(' ====== Exercício 13 ====== ')
# Solicitando ao usuário que insira o valor do salario que deve receber aumento.
salario = float(input('Qual é o salário do funcionário? R$'))
# Calculando o a soma do salario inserido com mais 15% de aumento.
novo = salario + (salario * 15/100)
# Exibindo o resultado ao usuário.
print('Um funcionário que ganhava {}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, novo))
