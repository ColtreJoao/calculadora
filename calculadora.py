while True:
    
    # Menu de opções
    print("\nEscolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    
    opcao = int(input("Digite o número da operação desejada: "))
    #Solicita ao usúario que insira dois números
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    # Realiza a operação escolhida e imprime o resultado
    if opcao == 1:
        resultado = num1 + num2
        print(f"A operação foi soma: {num1} + {num2} = {resultado}")
    elif opcao == 2:
        resultado = num1 - num2
        print(f"A operação foi subtração: {num1} - {num2} = {resultado}")
    elif opcao == 3:
        resultado = num1 * num2
        print(f"A operação foi multiplicação: {num1} * {num2} = {resultado}")
    elif opcao == 4:
        if num2 == 0:
            print("Erro: divisão por zero")
        else:
            resultado = num1 / num2
            print(f"A operação foi divisão: {num1} / {num2} = {resultado}")
    elif opcao == 5:
        print("Saindo da calculadora.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")