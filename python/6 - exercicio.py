import os
os.system('cls')

numero = int(input('Digite um número: '))

if numero < 10:
    print('É menor que 10!')
elif numero > 10:
    print('É maior que 10!')
else:
    print('É igual a 10!')