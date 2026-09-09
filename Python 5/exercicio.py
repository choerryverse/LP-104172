import os
os.system('cls')

print('=SOLICITANDO INFORMAÇÕES=')
matricula = int(input('\nInforme sua matrícula: '))
nascimento = int(input('Informe o ano do seu nascimento: '))
trabalho = int(input('Informe quantos anos você já trabalhou: '))
idade = 2026 - nascimento
print(f'\nMatrícula do empregado: {matricula}')
print(f'Idade: {idade} anos')
print(f'Tempo de trabalho: {trabalho} anos ')

if nascimento <= 1961 or trabalho >= 30:
    print('\nRequerer aposentadoria')
else:
    print('\nNão requerer aposentadoria')