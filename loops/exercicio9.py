import os
os.system('cls')

total_pagar = 0.0
resposta = "S"

precos = {
    1: 25.00,  # Picanha
    2: 20.00,  # Lasanha
    3: 18.00,  # Strogonoff
    4: 15.00,  # Bife Acebolado
    5: 5.00    # Pão com ovo
}

while resposta.upper() == "S":
    print("\n----- CARDÁPIO -----")
    print("1 - Picanha        - R$ 25,00")
    print("2 - Lasanha        - R$ 20,00")
    print("3 - Strogonoff     - R$ 18,00")
    print("4 - Bife Acebolado - R$ 15,00")
    print("5 - Pão com ovo    - R$ 5,00")
    print("--------------------")
    
    try:
        opcao = int(input("Escolha o código do prato desejado: "))
        if opcao in precos:
            total_pagar += precos[opcao]
            print(f"Item adicionado com sucesso!")
        else:
            print("Opção inválida! Tente novamente.")
    except ValueError:
        print("Entrada inválida! Digite apenas o número da opção.")

    resposta = input("\nDeseja escolher outro prato? (S/N): ")

print(f"\n==============================")
print(f"Total a pagar pelo cliente: R$ {total_pagar:.2f}")
print(f"==============================")