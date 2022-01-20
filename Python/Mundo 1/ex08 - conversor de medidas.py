print(' ====== Exercício 8 ====== ')
# Inserindo os metros, digitados pelo usuário, a uma variavel.
m = float(input('Digite os metros a serem convertidos: '))
# Calculando a equivalência dos metros para outras unidades de medida de comprimento.
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m / 1000
# Exibindo o resultado dos cálculos de medidas.
print('A medida de {} equivale a: \n{} Quilometros'.format(m, km))
print('{} Decâmetros \n{} Decímetros \n{} Centímetros \n{} Milímetros'.format(dam, dm, cm, mm))