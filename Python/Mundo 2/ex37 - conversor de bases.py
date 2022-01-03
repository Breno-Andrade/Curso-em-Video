# Coverte numero decimal para base escolhida pelo usuário.
print(' ====== Exercicio 37 ====== ')

# Solicitando valor para conversão.
num = int(input('Digite o numero a ser convertido: '))

# Exibindo as opções de bases para a conversão.
print('OPÇÕES DE CONVERSÃO')
print('[ 1 ] BINÁRIO\n[ 2 ] OCTAL\n[ 3 ] HEXADECIMAL\n')

# Atribuindo a escolha do usuário a uma variavel.
opção = int(input('\nEscolha a base pra conversão: '))

# Verificando e convertendo para a base escolhida.
if(opção == 1):
    # Obs. [2:] serve para remover os dois primeiro caracters da exibição.
    print('O valor {} em binário é: {}'.format(num, bin(num)[2:]))
elif(opção == 2):
    print('O valor {} em binário é: {}'.format(num, oct(num)[2:]))
elif(opção == 3):
    print('O valor {} em binário é: {}'.format(num, hex(num)[2:]))    
else:
    print('Opção invalida')
