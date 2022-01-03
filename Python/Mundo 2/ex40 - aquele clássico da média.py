#Calcula a media de um aluno e exibe sua situação.
print(' ====== Exercicio 40 ====== ')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

# Calcula a média.
media = (nota1 + nota2) / 2

print('O aluno que tirou {:.1f} e {:.1f} tem a média {:.1f}! Situação do aluno: '.format(nota1, nota2, media), end = '')

# Verifica a média e exibe a situação.
if(media < 5.0):
    print('Reprova!')
elif(media >= 5.0 and media < 7):
    print('Recuperação!')
else:
    print('Aprovado!')
