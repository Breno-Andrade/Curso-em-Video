# Classifica atleta de acordo com a idade.
print(' ====== Exercicio 41 ====== ')

# Atribuindo o ano atual a uma variavel.
from datetime import date
atual = date.today().year

nasc = int(input('Insira o ano de nascimento do atleta: '))

# Calculando a idade de acordo com o ano atual do sistema
idade = atual - nasc

# Exibindo a idade e a categoria do atleta.
print('\nQuem nasceu em {} tem {} anos em {}!'.format(nasc, idade, atual))

# Verificando e exibindo a categoria do atleta
print('Categoria do atleta: ', end = '')
if(idade <= 9):
    print('MIRIM')
elif(idade <= 14):
    print('INFANTIL')
elif(idade <= 19):
    print('JUNIOR')
elif(idade <= 20):
    print('SENIOR')
else:
    print('MASTER')
    