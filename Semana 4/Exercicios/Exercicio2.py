#Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.

numeroOriginal = input("Digite o valor de n: ")
numero = int(numeroOriginal) * 2
repeticao = 0

while repeticao <= numero - 1:
    repeticao = repeticao + 1
    if repeticao % 2 != 0:
        print(repeticao)
