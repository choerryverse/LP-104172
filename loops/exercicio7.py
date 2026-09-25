import os 
os.system('cls')

soma = 0

for i in range(1, 4):
    nota = float(input(f"Digite a {i}ª nota: "))
    soma += nota

media = soma / 3

print(f"\nA média das 3 notas é: {media:.2f}")

if media >= 7:
    print('ALUNO APROVADO')
elif media > 4 and media < 7:
    print('ALUNO EM RECUPERAÇÃO')
else:
    print('ALUNO REPROVADO')