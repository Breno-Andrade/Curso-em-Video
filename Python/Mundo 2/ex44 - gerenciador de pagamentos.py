# Calcula o valor a ser pago de acordo com a forma de pagamento
print(' ====== Exercicio 44 ====== ')

preço = float(input('Digite o valor do produto: '))
fp = str(input('Digite a forma de pagamento: ')).lower().strip()

if(fp == 'dinheiro' or fp == 'cheque'):
    vf = preço - ((preço * 10) / 100)
    print('\nVoce recebeu 10% de desconto!\nValor final a ser pago: {:.2f}'.format(vf))

elif(fp == 'cartão' or fp == 'cartao'):
    vzs = int(input('Digite a quantidade de parcelas: '))

    if(vzs == 1):
        vf = preço - ((preço * 5) / 100)
        print('\nVoce recebeu 5% de desconto!\nValor final a ser pago: {:.2f}'.format(vf))

    elif(vzs == 2):
        parcela = preço / vzs
        print('\nSua conta será parcelada em {}x de {:.2f}!'.format(vzs, parcela))
        print('Valor total: R${:.2f}'.format(preço))

    elif(vzs >= 3):
        vf = preço + ((preço * 20) / 100)
        parcela = vf / vzs
        print('\nSua compra será parcelada em {}x de {:.2f} com juros!'.format(vzs, parcela))
        print('O valor total do produto é {:.2f} com 20% de juros!'. format(vf))

    else:
        print('\nA quantidade minima de parcelas: 1x!')

else:
    print('\nforma de pagamento invalida')


