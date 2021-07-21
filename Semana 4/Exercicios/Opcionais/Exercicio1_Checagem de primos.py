# Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. 
# Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".

#Obs: usei o crivo de Eratóstenes.

numero = int(input("Digite um número inteiro: "))

if (numero <= 1) or (numero % 2 == 0 and numero !=2) or (numero % 3 == 0 and numero !=3) or (numero % 5 == 0 and numero != 5) or (numero % 7 == 0 and numero != 7):
    print("não primo")
else:
    print("primo")
