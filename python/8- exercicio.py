import os
os.system('cls')

primeiro_numero = float(input('Digite o primeiro número: '))
segundo_numero = float(input('Digite o segundo número: '))

soma = primeiro_numero + segundo_numero
produto = primeiro_numero * segundo_numero
media = (primeiro_numero + segundo_numero) / 2

print('\n= RESULTADOS =')
print(f'A soma é{soma: .2f}')
print(f'O produto é{produto: .2f}')
print(f'A média é{media: .2f}')

if primeiro_numero > segundo_numero:
    print('\nSeu primeiro número é maior que o segundo.')
else:
    print('\nSeu segundo número é maior que o primeiro.')