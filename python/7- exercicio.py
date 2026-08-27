import os
os.system ('cls')

primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a segunda nota: '))
terceira_nota = float(input('Digite a terceira nota: '))
media = (primeira_nota + segunda_nota + terceira_nota) / 3

if media >= 7:
    print(f'\nA média é {media: .2f} Aprovado.')
else:
    print(f'\nA média é {media: .2f} Reprovado.')