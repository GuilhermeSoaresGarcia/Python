#Dado número, você que tem que dizer se esse número tem dois dígitos adjacentes iguais

numero_original = input("Digite um número qualquer: ")
numero = int(numero_original)
resto = 1
novo_resto = 0

while resto != novo_resto:
    resto = numero % 10
    numero = numero // 10
    novo_resto = numero % 10
else:
    if numero == 0:
        print("O número", numero_original, "NÃO possui algarismos adjacentes")
    else:
        if novo_resto == resto:
            print("O número", numero_original, "possui um ou mais algarismos adjacentes iguais.")
