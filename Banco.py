menu = '''
[d]
[s]
[e]
[q]
=>
'''

saldo = 0
limite = 500
extrato = "0"
numero_saque = 0
LIMITE_SAQUE = 3


while True:

    opcao = input(menu)

    if opcao == "d":
        print("Deposito")
        dep = float(input("Qual valor que deseja depositar: "))

        if dep > 0:
            print("Deposito de {:.2f} realizado com sucesso" .format(dep))
            saldo += dep
            
        else:
            print("erro,valor incorreto, selecione novamente a opção desejada")



    elif opcao == "s":
        print("Saque")
        
        saque = float(input('informe o valor do saque: '))
        
        acima_saldo = saque > saldo
        acima_limite = saque > limite
        limite_saque = numero_saque >= LIMITE_SAQUE



        if acima_saldo:
            print('Saldo Insuficiente, tente novamente')

        elif limite_saque:
            print("Numero maximo de saques diarios, volte amanhã")
        
        elif acima_limite:
            print(' limite de saque diario de R$500,00 reais, digite outro valor')
        
        elif saque > 0:
            saldo -= saque
            extrato += 'saque: R$ {:.2f}'.format(saque)
            numero_saque += 1
        else:
            print("erro, selecione outra opção") 

    elif opcao == "e":
        print('não forão realizados movimentações' if not extrato else extrato)
        print("Saldo R$ {:.2f}".format(saldo))

    elif opcao == "q":
        break

    else:
        print("operação invalida, selecione novamente a operação desejada")     