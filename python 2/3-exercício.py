import os
os.system('cls')

print('= SOLICITANDO DADOS =')
nome = input('Informe o seu nome: ')
idade = int(input('Informe sua idade: '))

if idade < 16:
    print('\nVocê não pode votar.')
elif idade == 16 or idade == 17 or idade >= 65:
    print(f'\nSeu voto é facultativo, {nome}')
else:
    print('\nVocê é obrigado a votar.')