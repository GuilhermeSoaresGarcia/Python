numero_original = input("Insira um número qualquer: ")
numero = int(numero_original)

soma = 0

while numero > 0:
    resto = numero % 10
    numero = numero // 10
    soma = soma + resto
print("A soma de todos os algaritimos do número", numero_original, "é", soma)
