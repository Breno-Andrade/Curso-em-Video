from math import trunc

print(' ====== Exercício 16 ====== ')

print('Este programa solicita um numero real e exibe o valor inteiro do mesmo.')

num1 = float(input('Digite um numero real: '))
# usando módulo trunc para tranformar o numero real em numero inteiro.
print('O numero {} tem a parte inteira {}'.format(num1, trunc(num1)))