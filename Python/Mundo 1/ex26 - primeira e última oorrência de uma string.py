print(' ====== Exercicio 26 ====== ')

frase = str(input('Digite sua frase: ')).strip().lower()

# Contando quantas vezes aparece a letra A na frase.
print('Quantas vezes a letra A aparece na frase: \033[32m{}\033[m'.format(frase.count('a')))
# Identificando em qual posição aparece a primeira letra A na frase.
print('Em qual posição aparece a primeira letra A: \033[34m{}\033[m'.format(frase.find('a') + 1))
# Identificando em qual posição aparece a ultima letra A na frase.
print('Posição onde a letra A aparece pela ultima vez: \033[36m{}\033[m'.format(frase.rfind('a') + 1))
