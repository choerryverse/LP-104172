import os
os.system('cls')

print('A maçã custa R$ 1,30 porém ao comprar uma dúzia ou mais cada maçã sai por R$ 1,00.')
quantidade_de_macas = int(input('Quantas maçãs você deseja comprar ?: '))
if quantidade_de_macas >= 12:
    maca = 1.00
else:
    maca = 1.30

total = maca * quantidade_de_macas
print(f'Valor total: {total: .2f}')