import os
os.system('cls')

# ETAPA 1: Cadastro de Login e Senha
print("=== CADASTRO DE UTILIZADOR ===")
login_salvo = input("Cadastre o seu Login: ")
senha_salva = input("Cadastre a sua Senha: ")
print("Cadastro realizado com sucesso!\n")

# ETAPA 2: Sistema de Login com limite de 3 tentativas
tentativas = 0
max_tentativas = 3
autenticado = False

while tentativas < max_tentativas and not autenticado:
    tentativas += 1
    print(f"--- TENTATIVA {tentativas} DE {max_tentativas} ---")
    
    login_input = input("Digite o seu Login: ")
    senha_input = input("Digite a sua Senha: ")

    if login_input == login_salvo and senha_input == senha_salva:
        autenticado = True
        print("\nLogin efetuado com sucesso! Bem-vindo(a).")
    else:
        print("Login ou senha incorretos!\n")

if not autenticado:
    print("Número máximo de tentativas excedido! O programa foi finalizado.")