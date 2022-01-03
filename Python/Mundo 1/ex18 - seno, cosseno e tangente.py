from math import sin, cos, tan, radians

print(' ====== Exercício 18 ====== ') 
# Entrada de dados.
ang = float(input('Digite o ângulo: '))
# Utilizando os módulos (sin, cos e tan) para fazer o calculo. 
# Obs: Utilizamos o módulo radians para converter o grau para radiano.
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('O ângulo de {} tem o SENO de : {:.2f}'.format(ang, sen))
print('O ângulo de {} tem o COSSENO de: {:.2f}'.format(ang, cos))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, tan))