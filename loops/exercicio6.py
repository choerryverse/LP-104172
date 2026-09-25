import os 
os.system('cls')

soma = 0

for i in range(1, 5):
    nota = float(input(f"Digite a {i}ª nota: "))
    soma += nota

media = soma / 4
print(f"\nA média das 4 notas é: {media:.2f}")