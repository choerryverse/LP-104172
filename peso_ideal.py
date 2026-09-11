import os
os.system('cls')

peso = float(input('Digite seu peso atual: '))
altura = float(input('Digite sua altura: '))
genero = input('Informe seu gênero (M/F): ').upper()

match genero:
    case 'F':
        peso_ideal_F = (62.1 * altura) - 44.7
        print(f'\nSeu peso ideal é{peso_ideal_F: .1f}')
    case 'M':
        peso_ideal_M = (72.7 * altura) - 58
        print(f'\nSeu peso ideal é{peso_ideal_M: .1f}')
    case _:
        print('\nEscolha inválida, por favor escolha entre M e F.')