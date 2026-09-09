import os
os.system('cls')

dia = int(input('Digite o dia da semana: '))

match dia:
    case 1 | 7:
        print('Final de semana')
    case 2 | 3 | 4 | 5 | 6:
        print('Dia útil')
    case _:
        print('Inválido')