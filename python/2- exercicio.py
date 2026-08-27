import os
os.system('cls')

print('= SOLICITANDO DADOS =')
salario = float(input('Digite seu salário: '))
salario_minimo = 1621
resultado = salario / salario_minimo

print('\n= RESULTADO =')
print(f'Seu salário equivale a: {resultado:.2f} salários mínimos')