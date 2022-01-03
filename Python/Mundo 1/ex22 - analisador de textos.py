print(' ====== Exercicio 22 ====== ')

nome = str(input('Digite seu nome completo: ')).strip()

print('\n=============RESULTADO=============')
print('Seu nome em maiúsculo:', nome.upper()) # Exibe o nome em letras maiúsculas.
print('Seu nome em minúsculo:', nome.lower()) # Exibe o nome em letras minúsculas.
# Subtraindo a quantidade de letras pela quantidade de espaços
print('Quantidade de letras ao todo: {}'.format(len(nome) - nome.count(' '))) 
separa = nome.split()
print('Seu primeiro nome é: {}, e ele tem {} letras'.format(separa[0], len(separa[0])))
