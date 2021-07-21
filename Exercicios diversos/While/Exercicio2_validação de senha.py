# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input("Insira um nome de usuário: ")
senha = input("Insira uma senha: ")

while nome == senha:
    print("Nome e senha não podem ser iguais. Tente novamente.")
    senha = input("Insira uma senha: ")
print("OK!")
