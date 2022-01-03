# Verifica o ano de alistamento do usuário.
print(' ====== Exercicio 39 ====== ')

# Método para usar a data atual do sistema.
from datetime import date

nasc = int(input('Digite o ano do seu nascimento: '))

# Calculando a idade e o ano de alistamentoatravés da subtração do ano de nascimento pelo ano atual.
idade = date.today().year - nasc 
alis = date.today().year + (18 - idade)

# Exibindo a idade atual.
print('\nQuem nasceu em {} tem {} anos em {}!'.format(nasc, idade, date.today().year))

# Verificando e exibindo o ano para se alistar.
if(idade < 18):
    tempo = 18 - idade
    print('Voce deve se alistar em {}! Ainda faltam {} anos'.format(alis, tempo))
elif(idade == 18):
    print('Voce deve se alistar imediatamente!')
else:
    tempo = idade - 18
    print('Voce deveria ter se alistado em {}! Ja se passaram {} anos!\n'.format(alis, tempo))
