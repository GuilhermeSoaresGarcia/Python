numero = int(input("Digite um número inteiro: "))
resto = 1
novo_resto = 0

while resto != novo_resto:
    resto = numero % 10
    numero = numero // 10
    novo_resto = numero % 10
else:
    if numero == 0:
        print("não")
    else:
        if novo_resto == resto:
            print("sim")
