menu = ''' 
||::::...Menu Banco...::::||
       NÚMERO    ITEM        
        [1]     Depósito
        [2]     Extrato
        [3]     Saque
        [0]     Sair
||::::::::::::::::::::::::||

Número do Item: '''
#variaveris
saldo = 0
extrato_conta = ""
numero_de_saques = 0
limite_valor_diario = 1500
LIMITE_DE_SAQUES_DIARIOS = 3


while True:

        opcao = input (menu)

        if opcao == "1":
                valor = float(input('Quanto deseja Depositar: R$ '))
                if valor > 0:
                   saldo += valor
                   extrato_conta += f'Depósito de R$ {valor:.2f}\n'
                   print (f'Seu Saldo Atual é de: R$ {saldo:.2f}')
                else:
                        print ('\nValor inválido. Insira um valor positivo!\n')
                        
        elif opcao == "2":
                print("\n|||:::::::::....[EXTRATO]....:::::::::|||")
                print("Não foram realizadas movimentações." if not extrato_conta else extrato_conta)
                print(f"\nSaldo: R$ {saldo:.2f}")
                print("========================================")

        elif opcao == "3":
                valor = float(input('Qual valor deseja Sacar: R$ '))
        
                excedeu_saldo = valor > saldo
                excedeu_limite = valor > limite_valor_diario
                excedeu_saques = numero_de_saques >= LIMITE_DE_SAQUES_DIARIOS

                if excedeu_saldo:
                        print('\nVocê não tem saldo suficiente!\n')
                elif excedeu_limite:
                        print(f'\nO valor excede o limite máximo de saque por operação (R$ {limite_valor_diario:.2f})!\n')
                elif excedeu_saques:
                        print(f'\nVocê excedeu o número máximo de {LIMITE_DE_SAQUES_DIARIOS} saques diários!\n')
                elif valor > 0:
                        saldo -= valor
                        extrato_conta += f'Saque de R$ {valor:.2f}\n'
                        numero_de_saques += 1
                        print('\nSaque realizado com sucesso!\n')
                        print(f'Seu saldo atual é: R$ {saldo:.2f}\n')
                else:
                        print('\nValor inválido. Insira um valor positivo!\n')

        elif opcao == "0":
                break
        
        else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")
               