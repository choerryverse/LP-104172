import os
os.system('cls')

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
operador = input('Digite o operador (+, -, * ou /): ')

valido = True

match operador:
    case '+':
        resultado = num1 + num2
    case '-':
        resultado = num1 - num2
    case '*':
        resultado = num1 * num2
    case '/':
        resultado = num1 / num2
    case _:
        print('Operação inválida.')
        valido = False

if valido:
    print('\n--- Resultado ---')
    print(f'Primeiro número: {num1}')
    print(f'Segundo número: {num2}')
    print(f'Operador escolhido: {operador}')
    print(f'Resultado: {resultado}')