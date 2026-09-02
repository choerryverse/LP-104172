import os
os.system('cls')

peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura: '))
imc = peso / (altura * altura)
print(f'Seu IMC é {imc: .1f}')

if imc >= 40:
    print('\nOBESIDADE MÓRBIDA')
if imc >= 35:
    print('\nOBESIDADE SEVERA')
if imc >= 30:
    print('\nOBESIDADE GRAU 1')
if imc >= 25:
    print('\nLEVEMENTE ACIMA DO PESO')
if imc >= 18.6:
    print('\nPESO IDEAL')
if imc < 18.5:
    print('\nABAIXO DO PESO')
