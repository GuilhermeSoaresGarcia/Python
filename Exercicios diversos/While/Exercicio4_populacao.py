# # Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes
# # com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale 
# # a população do país B, mantidas as taxas de crescimento. 

# # Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação. 

paisA = int(input("Digite a menor população (país A): "))
crescimentoA = float(input("Digite o percentual de crescimento populacional do país A: "))
paisB = int(input("Digite a maior população (país B): "))
crescimentoB = float(input("Digite o percentual de crescimento populacional do país B: "))
anos = 0

while paisA >= paisB:
    print("A população do país B deve ser maior ou diferente da população do país A. Por favor, insira os dados novamente.")
    paisA = int(input("Digite a menor população (país A): "))
    paisB = int(input("Digite a maior população (país B): "))

while paisA <= paisB:
    paisA = paisA + (paisA * (crescimentoA / 100))
    paisB = paisB + (paisB * (crescimentoB / 100))
    anos += 1
print()
print("Após", anos, "anos, a população do país A igualou ou superou a população do país B.")
print("População do país A:", int(paisA))
print("População do país B:", int(paisB))
