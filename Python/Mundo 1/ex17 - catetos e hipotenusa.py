from math import hypot
print(' ====== Exercício 17 ====== ')

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
#hi = (ca ** 2 + co ** 2) ** (1/2)       #primeira opção sem utilizar biblioteca
hi = hypot(ca, co)                      #segunda opção utilizando biblioteca
print('A medida da hipotenusa é: {:.2f}'.format(hi))