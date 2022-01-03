# Compara dois valores e identifica o maior.
print(' ====== Exercicio 38 ====== ')

num1 = int(input('Digite um valor inteiro: '))
num2 = int(input('Digite outro valor inteiro: '))

# Verificando os dois valores para identificar qual o maior.
if(num1 > num2):
    print('\nO primeiro valor é o maior!')
elif(num2 > num1):
    print('\nO segundo valor é o maior!')
else:
    print('\nOs dois valores são iguais!')

