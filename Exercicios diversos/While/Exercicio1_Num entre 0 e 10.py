# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. 

numero = int(input("Insira uma nota entre 0 e 10: "))
numeroCorreto = (numero >= 0 and numero <= 10)

while numeroCorreto == False:
    numero = int(input("Este número não pertence ao intervalo solicitado. Insira novamente: "))
    numeroCorreto = (numero >= 0 and numero <= 10)
print("A nota informada foi", numero)
