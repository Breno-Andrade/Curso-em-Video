print(' ====== Exercicio 33 ====== ')

n1 = int(input("Digite o primero numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))
# atribuindo o ultimo valor a variavel (maior), dessa forma reduzimos um SE.
# Se n3 não for o maior valor então a variavel (maior) sera alterada.
maior = n3
# Verificando quem é o maior numero.
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
# Verificando quem é o menor numero.
menor = n3
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
print("O maior numero é: \033[32m{}\033[m".format(maior))
print("O menor numero é: \033[31m{}\033[m".format(menor))
