nome_banco = "Banco CO".center(32,"-")
boas_vindas = "Seja Bem Vindo!".center(32)

menu = f"""
{nome_banco}
{boas_vindas}
Selecione uma das opções abaixo:

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower()

    if opcao == "d": # DEPÓSITO
        while True: # Loop para o valor do depósito
            valor_deposito = input("Insira o valor que você deseja depositar: R$ ")
            if valor_deposito.isdigit():
                valor_deposito = float(valor_deposito)
                if valor_deposito > 0:
                    confirmacao = input(f"Você inseriu o valor de R$ {valor_deposito:.2f}?\nIsso está correto? (s/n): ").lower()
                    if confirmacao == 's':
                        saldo += valor_deposito
                        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
                        print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")

                        while True:# Loop para o retornar ao menu ou depositar novamente
                            retorno = input("\nDeseja realizar outro depósito (d) ou voltar ao menu inicial (i)?").lower()
                            match retorno:
                                case "d":
                                    break
                                case "i":
                                    break
                                case _: 
                                    print("Opção inválida. Por favor, digite 'd' para outro depósito ou 'i' para voltar ao menu.")
                            if retorno == "i": # Se o usuário escolheu 'i', sai do loop de depósito
                                break 
                        
                        if retorno == "i": # Se 'i' foi escolhido, pula o restante do loop de depósito
                            break 
                    else:
                        continue # Volta para pedir o valor do depósito novamente
                elif valor_deposito == 0:
                    print("Valor de depósito deve ser maior que zero.")
                else:
                    print("Valor de depósito deve ser positivo.")
            else:
                print("Valor de depósito inválido. Digite um número.")
    
        # Fim do loop de depósito
                                
    elif opcao == "s": # SAQUE
        while True:
            if numero_saques == LIMITE_SAQUES-1:
              print(f"""
        !!! ATENÇÃO !!!
Você já realizou {numero_saques} saques hoje.
Seu limite diário é de {LIMITE_SAQUES} saques.
Proceda com cuidado.


                    """)
            valor_saque = input("Insira o valor que você deseja sacar: R$ ")

            if valor_saque.isdigit():
                valor_saque = float(valor_saque)
                if valor_saque > 0:
                    confirmacao = input(f"Você inseriu o valor de R$ {valor_saque:.2f}?\nIsso está correto? (s/n): ").lower()
                    if confirmacao == 's':
                        if saldo == 0:
                            print("\nSua conta não possui saldo para saque.")
                            input("Pressione Enter para voltar ao menu inicial...") 
                            break
                        if valor_saque > saldo:
                            print(f"Saldo insuficiente. Seu saldo atual é R$ {saldo:.2f}.")
                            continue
                        if valor_saque > limite:
                            print(f"Valor de saque não pode ser maior que o limite de R$ {limite:.2f}.")
                            continue
                        if numero_saques >= LIMITE_SAQUES:
                            print(f"Você já realizou {LIMITE_SAQUES} saques hoje. Limite diário atingido.")
                            break
                        saldo -= valor_saque
                        extrato += f"   Saque: R$ {valor_saque:.2f}\n"
                        numero_saques += 1
                        print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")
                        
                        while True:# Loop para o retornar ao menu ou sacar novamente
                            retorno = input("\nDeseja realizar outro saque (s) ou voltar ao menu inicial (i)?").lower()
                            match retorno:
                                case "s":
                                    break 
                                case "i":
                                    break 
                                case _: 
                                    print("Opção inválida. Por favor, digite 's' para outro saque ou 'i' para voltar ao menu.")
                            if retorno == "i": # Se o usuário escolheu 'i', sai do loop de saque
                                break 
                        
                        if retorno == "i": # Se 'i' foi escolhido, pula o restante do loop de saque
                            break # Sai do loop de depósito para voltar ao menu principal
                    else:
                        continue 
                elif valor_saque == 0:
                    print("Valor de saque deve ser maior que zero.")
                else:
                    print("Valor de saque deve ser positivo.")
            else:
                print("Valor de saque inválido.")
        # Fim do loop de saque

    elif opcao == "e":
        print("\n================== EXTRATO ==================")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("=============================================\n")
        input("Pressione Enter para voltar ao menu inicial...") 
    elif opcao == "q":
        print("\n\nObrigado por utilizar nosso sistema.")
        print(nome_banco)
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")