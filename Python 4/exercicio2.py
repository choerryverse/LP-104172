import os
os.system('cls')

usuario = input('Informe o seu usuário: ')
media = float(input('Informe sua média: '))
faltas = int(input('Informe suas faltas: '))

if media >= 7 and faltas <= 40:
    print('\nUSUÁRIO APROVADO')
else:
    print('\nUSUÁRIO REPROVADO')