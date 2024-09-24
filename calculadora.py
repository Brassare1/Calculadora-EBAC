def calcular(operacao, num1, num2):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        return num1 / num2 if num2 != 0 else "Erro: Divisão por zero"
    
print('Bem-Vindo à minha Cálculadora Python!')

while True:
    print("\nEscolha a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    
    escolha = int(input('Escolha qual operação deseja realizar: '))
    
    if escolha == 5:
        print('\nObrigado por usar minha calculadora, volte sempre!')
        break   

    if escolha < 1 or escolha > 5:
        print('Operação inválida. Por favor, escolha uma opção válida!')
        continue    

    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    
    resultado = calcular(escolha, num1, num2)
    print(f'Resultado: {resultado}')
    