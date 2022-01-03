print(' ====== Exercício 4 ====== ')
# Atribuindo o valor digitado a variavel.
n1 = input('Digite algo: ')
# Dissecando a avariavel e exibindo o resultado.
print('O tipo primitivo desse valor é:', type(n1))
print('Só tem espaços?', n1.isspace())
print('É um numero?', n1.isnumeric())
print('É alfabético?', n1.isalpha())
print('São Alfanumérico?', n1.isalnum())
print('Está em maiúsculo?', n1.isupper())
print('Está em minúsculo?', n1.islower())
print('Está capitalizado?', n1.istitle())
