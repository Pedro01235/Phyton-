menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numeros_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).lower()  #Usei .lower() para garantir que a comparação seja case-insensitive

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}")
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    elif opcao == "s":
        if numeros_saques < LIMITE_SAQUES:
            valor = float(input("Informe o valor do saque: "))
            if valor > 0 and valor <= limite:
                if saldo >= valor:
                    saldo -= valor
                    numeros_saques += 1
                    extrato.append(f"Saque: R$ {valor:.2f}")
                    print("Saque realizado com sucesso!")
                else:
                    print("Saldo insuficiente.")
            else:
                print("Valor de saque inválido ou excede o limite por operação.")
        else:
            print("Limite de saques diários atingido.")

    elif opcao == "e":
        if extrato:
            print("\nExtrato de movimentações:")
            for mov in extrato:
                print(mov)
            print(f"Saldo atual: R$ {saldo:.2f}\n")
        else:
            print("Não foram realizadas movimentações.")

    elif opcao == "q":
        print("Sistema finalizado.")
        break

    else:
        print("Opção inválida. Tente novamente.")


#made by pedro
