# Calcula o IMC.
print(' ====== Exercicio 43 ====== ')

peso = float(input('Digite seu peso em quilos: '))
altura = float(input('digite sua altura em metros: '))

# Calculo do IMC.
imc = peso / (altura ** 2)

# verificando o IMC e exibindo o indice do usuário.
print('\nSeu IMC: {:.1f}'.format(imc))
print('Voce está em ', end = '')
if(imc <= 18.5):
    print('Abaixo do peso')
elif(imc < 25):
    print('Peso ideal')
elif(imc <= 30):
    print('Sobrepeso')
elif(imc <= 40):
    print('Obesidade')
else:
    print('Obesidade Mórbida')
