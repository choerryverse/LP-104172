import os
os.system('cls')

primeiro_numero = float(input('Digite seu primeiro número: '))
segundo_numero = float(input('Digite seu segundo número: '))
terceiro_numero = float(input('Digite seu terceiro número: '))

maior = max(primeiro_numero, segundo_numero, terceiro_numero)
menor = min(primeiro_numero, segundo_numero, terceiro_numero)

print(f'Números selecionados: {primeiro_numero} e {segundo_numero} e {terceiro_numero}')
print('Maior número: ', maior)
print('Menor número: ', menor)