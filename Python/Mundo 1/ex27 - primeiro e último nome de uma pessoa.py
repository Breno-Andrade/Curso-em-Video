print(' ====== Exercicio 27 ====== ')

nome = str(input('Digite seu nome completo: ')).strip().split()
cont = len(nome)
print('É um prazer te conhecer!')
# Identificando o primeiro nome e exibindo.
print('Seu primeiro nome é: {}'.format(nome[0]))
# Identificando o Ultimo nome e exibindo.
print('Seu ultimo nome é: {}'.format(nome[len(nome) - 1]))
