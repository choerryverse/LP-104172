import os
os.system('cls')

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
operador = input('Digite o operador (+, -, * ou /): ')

valido = True

if operador == '+':
    resultado = num1 + num2
elif operador == '-':
    resultado = num1 - num2
elif operador == '*':
    resultado = num1 * num2
elif operador == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        print('Erro: Divisão por zero não é permitida.')
        valido = False
        
else:
    print('Operador inválido.')

if valido:
    print('\n--- Resultado ---')
    print(f'Primeiro número: {num1}')
    print(f'Segundo número: {num2}')
    print(f'Operador escolhido: {operador}')
    print(f'Resultado: {resultado}')