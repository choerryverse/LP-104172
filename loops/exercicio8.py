import os
os.system('cls')

login_correto = "camilla"
senha_correta = "1234"

while True:
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")

    if login == login_correto and senha == senha_correta:
        print("Acesso concedido! Bem-vindo.")
        break  # Encerra o loop quando ambos estiverem corretos
    else:
        print("Login ou senha incorretos. Tente novamente.\n")