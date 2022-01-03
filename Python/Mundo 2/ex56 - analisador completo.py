idadetotal = 0
médiaidade = 0
maioridadeM = 0
nomeH = ''
totmulher = 0

for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    idadetotal += idade

    if p == 1 and sexo == 'M':
        maioridadeM = idade
        nomeH = nome
    
    if idade > maioridadeM and sexo == 'M':
        maioridadeM = idade
        nomeH = nome

    if idade < 20 and sexo == 'F':
        totmulher += 1
    
        

médiaidade = idadetotal / 4
print('A média de idade do grupo é: {}'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadeM, nomeH))
print('{} mulheres tem menos de 20 anos de idade'.format(totmulher))

