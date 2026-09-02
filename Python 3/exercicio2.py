import os
os.system('cls')

print('=SOLICITANDO INFORMAÇÕES=')
nome = input('Digite o seu nome: ')
primeira_nota = float(input('Digite sua primeira nota: '))
segunda_nota = float(input('Digite sua segunda nota: '))
media = (primeira_nota + segunda_nota) / 2

print(f'\nNome: {nome}')
print(f'\nMédia: {media: .1f}')

if media >= 9:
    print('Seu conceito é A.')
elif media >= 7.5:
    print('Seu conceito é B.')
elif media >= 6:
    print('Seu conceito é C.')
elif media >= 4:
    print('Seu conceito é D.')
else:
    print('Seu conceito é E.')

if media >= 6:
    print('APROVADO')
else:
    print('REPROVADO')