import os
os.system('cls')

print("=" * 35)
print("         CARDÁPIO DO RESTAURANTE")
print("=" * 35)
print("Código | Prato           | Valor")
print("   1   | Picanha         | R$ 25,00")
print("   2   | Lasanha         | R$ 20,00")
print("   3   | Strogonoff      | R$ 18,00")
print("   4   | Bife Acebolado  | R$ 15,00")
print("   5   | Pão com ovo     | R$  5,00")
print("=" * 35)

codigo = int(input('\nDigite o código do prato desejado: '))

valido = True

match codigo:
    case 1:
        prato = 'Picanha'
        valor = 25.00
    case 2:
        prato = 'Lasanha'
        valor = 20.00
    case 3:
        prato = 'Strogonoff'
        valor = 18.00
    case 4:
        prato = 'Bife Acebolado'
        valor = 15.00
    case 5:
        prato = 'Pão com ovo'
        valor = 5.00
    case _:
        print('\nCódigo inválido! Por favor, escolha uma opção de 1 a 5.')
        valido = False

if valido:
    print('\n--- Prato Escolhido ---')
    print(f'Prato: {prato}')
    print(f"Valor: R$ {valor: .2f}")