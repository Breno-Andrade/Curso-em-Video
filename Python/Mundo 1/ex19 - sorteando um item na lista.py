from random import choice

print(" ====== Exercicio 19 ====== ")
# Entrada de dados
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
# Atribuindo os nomes em uma lista.
lista = [n1, n2, n3, n4]
# Escolhendo um nome aleatorio da lista e atribuindo a variavel(escolhido).
escolhido = choice(lista)
# Exibindo o nome escolhido.
print('O escolhido foi {}'.format(escolhido))