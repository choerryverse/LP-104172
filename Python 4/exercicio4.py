import os
os.system('cls')

numero = float(input('Digite sua nota: '))

if numero >= 0 and numero <= 10:
    print(f'\nSua nota é {numero}.')
else:
    print('\nSua nota deve estar entre 0 e 10.')