# Analisas os lados inseridos e verifica se pode ser um triângulo, caso seja, informa qual.
print(' ====== Exercicio 42 ====== ')

s1 = float(input('Insira o primeiro segmento: '))
s2 = float(input('Insira o segundo segmento: '))
s3 = float(input('Insira o terceiro segmento: '))

# Verifica se a soma de dois dos lados é maior que o ultimo.
if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print('\nOs segmentos formam um triângulo: ',  end = '')

    # Verificando qual a forma do triângulo através das propriedades.
    if s1 == s2 and s2 == s3:
        print('Equilátero')
    elif s1 != s2 and s1 != s3 and s2 != s3:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('\nOs segmentos não correspodem a um triângulo!')
