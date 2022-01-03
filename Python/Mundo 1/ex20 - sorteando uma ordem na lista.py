#Exibe uma lista de forma randômica dos nomes inseridos.
from random import shuffle

print(' ====== Exercicio 20 ====== ')
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))
# Adicionando os valores a uma lista.
lista = [n1, n2, n3, n4]
# Usando o Módulo Shuffle para embaralhar a lista. 
shuffle(lista)
# Exibindo o resultado da lista embaralhada.
print('A ordem de apresentação sera: ')
print(lista)
