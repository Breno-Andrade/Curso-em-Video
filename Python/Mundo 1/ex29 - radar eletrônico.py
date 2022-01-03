print(' ====== Exercicio 29 ====== ')

velocidade = float(input("Digite sua velocidade atual: "))
if velocidade > 80:
    multa = (velocidade - 80) * 7.00
    print("\033[31mMULTADO\033[m! \033[4mVoce excedeu o limite que é de\033[m \033[4;31m80km/h\033[m")
    print("Voce foi \033[31mMULTADO\033[m!! \033[4;31mSua multa e de {:.2f} reais\033[m.".format(multa))
print("Tenha um bom dia! \033[32mDirija com segurança\033[m!")